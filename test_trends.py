"""Test trends endpoint directly"""
import sys
sys.path.insert(0, 'c:\\Users\\Bruger\\OneDrive\\Desktop\\NLP')

from src.api.main import generate_sample_trends

print("Testing trends endpoint...")
print("=" * 70)

try:
    trends = generate_sample_trends()
    
    print(f"✅ Trends generated successfully!")
    print(f"✅ Number of diseases: {len(trends)}")
    print(f"✅ Diseases: {', '.join(trends.keys())}")
    
    print("\n📈 Sample trend data:")
    for disease, data in trends.items():
        print(f"\n{disease}:")
        print(f"  - Days of data: {len(data['data'])}")
        print(f"  - Latest count: {data['data'][-1]['count']}")
        print(f"  - Latest date: {data['data'][-1]['date']}")
    
    print("\n" + "=" * 70)
    print("✅ TRENDS ENDPOINT WORKING!")
    print("=" * 70)
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
