from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
import os
#Make sure u mount google drive so the ouputs save in google drive automatically.
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://Your facefusion url/")
        self.sleep(10)
        self.js_click('span:contains("face_enhancer")')
        self.sleep(5)
        self.js_click('span:contains("frame_enhancer")')
        self.sleep(5)
        self.type('input[aria-label="FACE SWAPPER PIXEL BOOST"]', "1024x1024")
        self.send_keys('input[aria-label="FACE SWAPPER PIXEL BOOST"]', Keys.ENTER) 
        self.click("div#component-2")
        file_path1 = r"C:\SourceTarget\2.png"
        self.execute_script("""
            const inputs = Array.from(document.querySelectorAll('input[data-testid="file-upload"]'));
            if (!inputs.length) throw new Error('No file-upload inputs found');
            // give each input a predictable id and unhide it
            inputs.forEach((el, i) => {
                el.id = 'file-upload-' + (i+1);
                el.style.display = 'block';
                el.style.visibility = 'visible';
                el.style.opacity = '1';
                // remove pointer-events:none if present
                el.style.pointerEvents = 'auto';
            });
        """)
        self.send_keys('#file-upload-1', file_path1)
        target_dir = r"C:\target dir\where all images are\"
        targets = [os.path.join(target_dir, f) for f in os.listdir(target_dir)
                if f.lower().endswith('.jpeg')]
        targets.sort()
        for file_path2 in targets:
            self.execute_script("""
                const inputs = Array.from(document.querySelectorAll('input[data-testid="file-upload"]'));
                if (!inputs.length) return;
                inputs.forEach((el, i) => {
                    el.id = 'file-upload-' + (i+1);
                    el.style.display = 'block';
                    el.style.visibility = 'visible';
                    el.style.opacity = '1';
                    el.style.pointerEvents = 'auto';
                });
            """)
            try:
                self.wait_for_element('#file-upload-2', timeout=20)
            except Exception as e:
                self.execute_script("""
                    const inputs = Array.from(document.querySelectorAll('input[data-testid="file-upload"]'));
                    inputs.forEach((el, i) => el.id = 'file-upload-' + (i+1));
                """)
                self.wait_for_element('#file-upload-2', timeout=15)
            self.execute_script("const el = document.querySelector('#file-upload-2'); if (el) el.value = '';")
            self.send_keys('#file-upload-2', file_path2)
            self.execute_script("document.querySelector('#file-upload-2')?.dispatchEvent(new Event('change', { bubbles: true }));")
            self.type('input[aria-label="number input for OUTPUT IMAGE QUALITY"]', "100")
            self.send_keys('input[aria-label="number input for OUTPUT IMAGE QUALITY"]', Keys.ENTER)
            self.sleep(10)
            self.click("button#component-113")
            self.sleep(20)
            self.click("button#component-115")
            self.click("div#component-97 > div:nth-of-type(2) > button > div > svg > path")
