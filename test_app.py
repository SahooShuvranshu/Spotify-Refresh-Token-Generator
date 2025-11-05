"""
Simple test to verify the Token Generator app works
Run: python test_app.py
"""

def test_imports():
    """Test that all required imports work"""
    try:
        from flask import Flask, render_template, request, jsonify, redirect
        import requests
        from base64 import b64encode
        from urllib.parse import quote
        import os
        print("✅ All imports successful!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_app_creation():
    """Test that Flask app can be created"""
    try:
        import app
        print("✅ Flask app created successfully!")
        return True
    except Exception as e:
        print(f"❌ App creation error: {e}")
        return False

def test_routes():
    """Test that all routes are defined"""
    try:
        import app as flask_app
        routes = [rule.rule for rule in flask_app.app.url_map.iter_rules()]
        expected_routes = ['/', '/start', '/callback', '/exchange', '/health']
        
        for route in expected_routes:
            if route in routes:
                print(f"✅ Route {route} exists")
            else:
                print(f"❌ Route {route} missing")
                return False
        
        print("✅ All routes defined!")
        return True
    except Exception as e:
        print(f"❌ Route test error: {e}")
        return False

def test_templates():
    """Test that template files exist"""
    import os
    try:
        templates = ['templates/index.html', 'templates/callback.html']
        for template in templates:
            if os.path.exists(template):
                print(f"✅ Template {template} exists")
            else:
                print(f"❌ Template {template} missing")
                return False
        
        print("✅ All templates found!")
        return True
    except Exception as e:
        print(f"❌ Template test error: {e}")
        return False

if __name__ == '__main__':
    print("🧪 Testing Spotify Token Generator...\n")
    
    tests = [
        ("Imports", test_imports),
        ("App Creation", test_app_creation),
        ("Routes", test_routes),
        ("Templates", test_templates)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n📋 Testing {test_name}...")
        if test_func():
            passed += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"✅ Passed: {passed}/{len(tests)}")
    print(f"❌ Failed: {failed}/{len(tests)}")
    
    if failed == 0:
        print("\n🎉 All tests passed! Ready to deploy!")
    else:
        print("\n⚠️ Some tests failed. Fix them before deploying.")
