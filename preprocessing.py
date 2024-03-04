import tensorflow_transform as tft

def preprocessing_fn(inputs):
    outputs = {}
    
    # Escalar características numéricas con z score
    for feature in ['Elevation', 'Slope', 'Horizontal_Distance_To_Hydrology',
                    'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
                    'Hillshade_9am', 'Hillshade_Noon', 'Horizontal_Distance_To_Fire_Points']:
        outputs[feature] = tft.scale_to_z_score(inputs[feature])
    
    outputs['Soil_Type'] = tft.hash_strings(inputs['Soil_Type'], hash_buckets=80)
    
    # Convertir características categóricas en índices de vocabulario
    outputs['Wilderness_Area'] = tft.compute_and_apply_vocabulary(inputs['Wilderness_Area'])
    # No transformar la etiqueta
    outputs['Cover_Type'] = inputs['Cover_Type']
    
    return outputs