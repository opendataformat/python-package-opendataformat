# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:12:37 2024

@author: thartl
"""

import pandas as pd


def docu_odf(x, metadata = "all", languages = "all"):
    """
    Extract and display metadata from a pandas DataFrame or pandas.Series.

    This function processes the metadata stored in the `attrs` attribute of a pandas object,
    allowing for selective extraction by metadata type or language. Metadata includes fields
    such as labels, descriptions, and URLs.

    Parameters
    ----------
    x : pandas.DataFrame or pandas.Series (single variable metadata)
        The input pandas object from which metadata will be extracted.
    metadata : str, default "all"
        The type of metadata to extract. Options include:
        - "all": Extract and display all available metadata.
        - "label", "labels": Extract value labels.
        - "description": Extract descriptions.
        - "type": Extract types.
        - "url": Extract URLs.
        Aliases for these options are supported (e.g., "Value labels" for "labels").
    languages : str or list of str, default "all"
        The language(s) to filter metadata by. Options include:
        - "all": Process metadata for all languages.
        - A single language code (e.g., "en").
        Edge cases like empty strings or None are handled gracefully.

    Returns
    -------
    dict or str
        Extracted metadata as a dictionary. If only a single metadata field is found,
        returns the metadata as a string instead.

    Raises
    ------
    TypeError
        If `x` is not a pandas DataFrame or Series.
    ValueError
        If `metadata` or `languages` contain invalid values.

    Notes
    -----
    - Metadata is stored in the `attrs` attribute of pandas objects.
    - This function supports multilingual metadata if provided in the input.

    Examples
    --------
    Extract dataset level metadata from a DataFrame:

    >>> df = read_odf("example_dataset.zip")
    >>> df.attrs
    >>> docu_odf(df)
    
    Extract specific variable metadata:

    >>> docu_odf(df['variable_name'])

    Extract specific metadata type:

    >>> docu_odf(df, metadata="label")


    Extract metadata filtered by language:

    >>> docu_odf(df, metadata="label", languages="en")
    label_en: English Label
    """
    
    if not isinstance(x, (pd.DataFrame, pd.Series)):
        TypeError('x is not a pandas data frame or a columns of a pandas data frame')
        
        
    # convert anlanguages to a list or if languages = ["all"] unlist it
    if languages != "all" and not isinstance(languages, list):
        languages = [languages]
    
    if isinstance(languages, list) and len(languages) == 1:
        if languages[0] == "all":
            languages = languages[0]        
    if isinstance(languages, list) and (None in languages or '' in languages):
        languages += ["label", "labels", "description"]
    
    if languages != "all" and not isinstance(languages, list):
        raise ValueError("languages  not valid")

    if metadata=='all':
        for key, value in x.attrs.items():
            if key in ['dataset', 'url']:
                print(f'{key}: {value}')
            elif 'labels' in key:
                if (languages == 'all'):
                    if key == 'labels':
                        lang = ''
                    else:
                        lang = key.split('_')[-1]
                    print(f'Value Labels {lang}:')
                    for val, lab in value.items():
                        print(f'{val}:   {lab}')
                else:
                    if key.split('_')[-1] in languages:
                        print(f'Value Labels {key.split("_")[-1]}:')
                        for val, lab in value.items():
                            print(f'{val}:   {lab}')
            else:
                if (languages == 'all'):
                    print(f'{key}: {value}')
                else:
                    if key.split('_')[-1] in languages:
                        print(f'{key}: {value}')
    else:
        if metadata in ['Labels', 'labels', 'label', 'Label']:
            metadata = 'label'
        elif metadata in ['description', 'Description', 'Descriptions', 'Descriptions']:
            metadata = 'description'
        elif metadata in ['valuelabels', 'valuelabels', 'valuelabel', 
                        'value labels', 'value label', 'Valuelabels', 
                        'Valuelabel', 'Value labels', 'Value Label']:
            metadata = 'labels'
        elif metadata in ['type', 'Type', 'types', 'Types']:
            metadata = 'type'
        elif metadata in ['URL', 'url', 'URI', 'uri']:
            metadata = 'url'
        else:
            raise ValueError('metadata must be one of following options: "all", "label", "labels", "description", "descriptions", "valuelabel", "valuelabels", "type", "types", "url"')
        output = {}                    
        if languages == 'all':
            for key, value in x.attrs.items():
                if key == metadata or key.startswith(metadata + "_"):
                    if metadata == 'labels':
                        print(f'Value {key.replace("_", " ")}:')
                        for k,v in value.items():
                            print(k + ":  " + v)
                        output[key] = value
                    else:
                        print(key + ': ' + value)
                        output[key] = value
        else:
            if metadata in ['label', 'description', 'labels']:
                for lang in languages:
                    if lang not in ['label', 'description', 'labels']:
                        if metadata != 'labels':
                            if lang != None and lang != '':
                                print(metadata + '_' + lang + ':  ' + x.attrs.get(metadata + '_' + lang, 'Not found'))
                                output[metadata + '_' + lang] = x.attrs.get(metadata + '_' + lang, 'Not found')
                            else:
                                print(metadata + ':  ' + x.attrs.get(metadata, 'Not found'))
                                output[metadata] = x.attrs.get(metadata, 'Not found')
                        else:
                            if lang != None and lang != '':
                                if isinstance(x.attrs.get(metadata + '_' + lang, None), dict):
                                    print(f'Value labels {lang}:')
                                    for val,lab in x.attrs.get(metadata + '_' + lang, {}).items():
                                        if (lab == None):
                                            lab = 'None'
                                        print(val + ":  " + lab)
                                else:
                                    print(f'Value labels {lang} not found')
                                output[metadata + '_' + lang] = x.attrs.get(metadata + '_' + lang, 'Not found')
                            else:
                                if isinstance(x.attrs.get(metadata, None), dict):
                                    print('Value labels:')
                                    for val,lab in x.attrs.get(metadata, {}).items():
                                        print(val + ":  " + lab)
                                else:
                                    print('Value labels without language tag not found')
                                output[metadata] = x.attrs.get(metadata, 'Not found')
                                
                                for val, lab in value.items():
                                    print(f'{val}:   {lab}')
            else:
                print(metadata + ':  ' + x.attrs.get(metadata, 'Not found'))
                output[metadata] = x.attrs.get(metadata, 'Not found')
        if output == {}:
            print('Metadata ' + metadata + ' not found')
        # if we have only one output, return the output as string instead of as dictionary
        if len(output) == 1:
            output = next(iter(output.values()))
        return output
        
    
    
