import {setTimeout} from "node:timers/promises";
import fs from 'fs';
import { launch } from 'puppeteer';

function generateUrls(vidList) {
    const baseUrl = 'https://v.qq.com/x/cover/c5u86fwtyyoch4r/';
    const queryParams = '?ptag=2345.tv';
    
    const urls = vidList.map(vid => `${baseUrl}${vid}.html${queryParams}`);
    
    return urls;
}

const vidList = [
    "s0026lqv9xm","i00261lbqe5","b0026frtg0n","n00262fi073","k0026ft5p03",
    "w0026vxmk59","w0026hfavkh","b002694ovtt","l00262uzioc","f0026obr7bx",
    "c00265m7yxq","g0026jqhj40","y0026mp9gpc","z0026opzyfd","g0026sto6p8",
    "v0026han9tv","v0026s8k914","e0026z3kwoh","j0026yb0qck","h00267jks3n",
    "j0026zidi22","q002658e8z5","t0026zthg6f","b002675qmlz","e0026vdxfps",
    "k00263xgshv","t0026i9h3hv","w00263zro6w","e0026u316c5","q0026d8pmg9",
    "z0026bdbeuj","p0026owqlq5","d0026gcszem","w00264811b7","r0026g7em80"
];

const urls = generateUrls(vidList);

(async () => {
    const browser = await launch({ headless: true });
    const page = await browser.newPage();

    for (const [index, url] of urls.entries()) {
        page.on('response', async (response) => {
            const responseUrl = response.url();
            if (responseUrl.includes('m3u8')) {
                try {
                    const text = await response.text();
                    console.log('URL:', responseUrl);
                    fs.writeFileSync(`./responses/response_${index}.txt`, `URL: ${responseUrl}\nResponse: ${text}\n\n`, { flag: 'a' });
                } catch (err) {
                    console.error('Error fetching response:', err);
                }
            }
        });

        await page.goto(url, { waitUntil: 'networkidle2' });
        await setTimeout(10000);

        page.removeAllListeners('response');
    }

    await browser.close();
})();
