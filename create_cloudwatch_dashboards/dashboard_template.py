def get_dashboard_body(device_id):
    return f"""
{{
    "widgets": [
        {{
            "height": 6,
            "width": 18,
            "y": 0,
            "x": 0,
            "type": "metric",
            "properties": {{
                "view": "gauge",
                "metrics": [
                    [ "NoiseSensors/Monitoring", "dblevel", "DeviceId", "{device_id}" ],
                    [ ".", "batteryV", ".", "." ],
                    [ ".", "sigStrength", ".", "." ],
                    [ ".", "panelV", ".", "." ]
                ],
                "region": "eu-west-1",
                "yAxis": {{
                    "left": {{
                        "min": 0,
                        "max": 200
                    }}
                }},
                "stat": "Average",
                "period": 30,
                "title": "Metrics"
            }}
        }},
        {{
            "height": 6,
            "width": 6,
            "y": 0,
            "x": 18,
            "type": "metric",
            "properties": {{
                "metrics": [
                    [ {{ "expression": "LAST(m1)", "label": "Expression1", "id": "e1", "visible": false, "period": 30 }} ],
                    [ "NoiseSensors/Monitoring", "dataBalance", "DeviceId", "{device_id}", {{ "id": "m1" }} ]
                ],
                "view": "gauge",
                "region": "eu-west-1",
                "yAxis": {{
                    "left": {{
                        "min": 0,
                        "max": 10000
                    }}
                }},
                "stat": "Average",
                "period": 30,
                "liveData": true
            }}
        }},
        {{
            "height": 6,
            "width": 18,
            "y": 6,
            "x": 0,
            "type": "metric",
            "properties": {{
                "metrics": [
                    [ "NoiseSensors/Monitoring", "dblevel", "DeviceId", "{device_id}", {{ "region": "eu-west-1" }} ]
                ],
                "view": "timeSeries",
                "stacked": false,
                "region": "eu-west-1",
                "stat": "Average",
                "period": 60,
                "title": "DB Level Graph"
            }}
        }}
    ]
}}
"""
