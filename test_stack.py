import sys 

print(f"Python: {sys.version}") 

try: 
    import docling 
    
    print("✅ Docling (Document Intelligence) is READY.") 
    

except ImportError: print("❌ Docling is MISSING.") 

try: 
    import langflow 
    
    print("✅ Langflow (Visual Agents) is READY.") 
    
except ImportError: print("❌ Langflow is MISSING.") 

try: 
    from ibm_watsonx_ai import APIClient 
    print("✅ IBM Watsonx SDK is READY.") 
    
except ImportError: print("❌ Watsonx SDK is MISSING.")