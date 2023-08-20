#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

# Dictionary of Indian states and their capitals
indian_states_capitals = {
    "Manipur": "Imphal",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Sikkim": "Gangtok",
    "Rajasthan": "Jaipur"
}

# Write the dictionary to a JSON file
with open('indian_states_capitals.json', 'w') as json_file:
    json.dump(indian_states_capitals, json_file, indent=4)

print("JSON file 'indian_states_capitals.json' created successfully!")

