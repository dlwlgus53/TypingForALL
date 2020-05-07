import json

json_data = json.dump({
  "results": [
    {
      "alternatives": [
        {
          "confidence": 0.43,
          "transcript": "true the specter the group "
        }
      ],
      "final": true

  ],
  "result_index": 0
})

  
gender, gen_confidence = json_data['faces'][0]['gender'].values() # 성별 
age, age_confidence = json_data['faces'][0]['age'].values() # 나이 
emotion, emotion_confidence = json_data['faces'][0]['emotion'].values() # 감정 

print(gender )
# result = """ 
# 성별: %s  
# 나이: %s  
# 감정: %s  
# """ % ( 
#     gender, 
#     age,  
#     emotion
# )


