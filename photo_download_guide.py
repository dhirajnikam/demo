import pandas as pd
import os
import webbrowser
import time

def create_photo_download_guide():
    """
    Create a comprehensive guide for downloading faculty photos
    """
    
    # Read Excel data
    df = pd.read_excel('CREED Faculty Members.xlsx', sheet_name='Sheet1')
    
    print("🎯 CREED Faculty Photo Download Guide")
    print("=" * 60)
    print()
    
    # Faculty who need actual photos (currently using placeholder/incorrect images)
    faculty_needing_photos = [
        'Dr. Sarang Gumfekar',
        'Dr. Chander Shekhar Sharma', 
        'Dr. Asad H. Sahir',
        'Dr T.V. Kalyan'
    ]
    
    print("📋 FACULTY MEMBERS NEEDING ACTUAL PHOTOS:")
    print("-" * 40)
    
    for i, faculty_name in enumerate(faculty_needing_photos, 1):
        print(f"{i}. {faculty_name}")
    
    print()
    print("🔗 LINKEDIN PROFILES TO VISIT:")
    print("-" * 40)
    
    for i, row in df.iterrows():
        if i > 0:  # Skip header row
            name = row.iloc[1].strip()
            linkedin = row.iloc[4]
            
            if pd.notna(linkedin) and name in faculty_needing_photos:
                linkedin_url = linkedin.strip()
                print(f"• {name}: {linkedin_url}")
    
    print()
    print("📥 MANUAL DOWNLOAD STEPS:")
    print("-" * 40)
    print("1. Visit each LinkedIn profile above")
    print("2. Right-click on the profile photo")
    print("3. Select 'Save image as...'")
    print("4. Save with the correct filename in the appropriate directory")
    print()
    
    print("📁 SAVE LOCATIONS:")
    print("-" * 40)
    
    for i, row in df.iterrows():
        if i > 0:  # Skip header row
            name = row.iloc[1].strip()
            linkedin = row.iloc[4]
            
            if pd.notna(linkedin) and name in faculty_needing_photos:
                # Clean name for filename
                clean_name = name.replace(' ', '_').replace('.', '').replace(',', '')
                clean_name = clean_name.replace('Dr_', 'Dr_').replace('Prof_', 'Prof_')
                
                if name in ['Dr. Sarang Gumfekar', 'Dr. Chander Shekhar Sharma', 'Dr. Asad H. Sahir']:
                    save_path = f"faculty_photographs/CREED_Faculty/{clean_name}.jpg"
                else:
                    save_path = f"faculty_photographs/KISEM_Technical/{clean_name}.jpg"
                
                print(f"• {name}: {save_path}")
    
    print()
    print("🔄 HTML UPDATE REQUIRED:")
    print("-" * 40)
    print("After downloading photos, update the HTML file to use the new photo paths:")
    print()
    
    for i, row in df.iterrows():
        if i > 0:  # Skip header row
            name = row.iloc[1].strip()
            linkedin = row.iloc[4]
            
            if pd.notna(linkedin) and name in faculty_needing_photos:
                clean_name = name.replace(' ', '_').replace('.', '').replace(',', '')
                clean_name = clean_name.replace('Dr_', 'Dr_').replace('Prof_', 'Prof_')
                
                if name in ['Dr. Sarang Gumfekar', 'Dr. Chander Shekhar Sharma', 'Dr. Asad H. Sahir']:
                    html_path = f"faculty_photographs/CREED_Faculty/{clean_name}.jpg"
                else:
                    html_path = f"faculty_photographs/KISEM_Technical/{clean_name}.jpg"
                
                print(f"• {name}: Update img path to '{html_path}'")
    
    print()
    print("🚀 AUTOMATED BROWSER OPENING:")
    print("-" * 40)
    print("Opening LinkedIn profiles in your default browser...")
    print()
    
    # Open LinkedIn profiles in browser
    for i, row in df.iterrows():
        if i > 0:  # Skip header row
            name = row.iloc[1].strip()
            linkedin = row.iloc[4]
            
            if pd.notna(linkedin) and name in faculty_needing_photos:
                linkedin_url = linkedin.strip()
                print(f"Opening: {name} - {linkedin_url}")
                webbrowser.open(linkedin_url)
                time.sleep(2)  # Wait between opening tabs
    
    print()
    print("✅ COMPLETION CHECKLIST:")
    print("-" * 40)
    print("□ Download photos for all 4 faculty members")
    print("□ Save photos with correct filenames in correct directories")
    print("□ Update HTML file with new photo paths")
    print("□ Test website to ensure photos display correctly")
    print("□ Verify all faculty members have proper photos")
    
    print()
    print("🎉 Once completed, all faculty members will have their actual photos!")

if __name__ == "__main__":
    create_photo_download_guide()
