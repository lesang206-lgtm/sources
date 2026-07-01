// ============ TAB SWITCHING ============
let currentTab = 'modle';

document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        btn.classList.add('active');
        const tab = btn.dataset.tab;
        currentTab = tab;
        document.getElementById('tab-' + tab).classList.add('active');
        const search = document.getElementById('searchInput');
        if (tab === 'modle') { search.placeholder = 'Tìm tướng hoặc skin...'; filterHeroes(); }
        else if (tab === 'modpack') { search.placeholder = 'Tìm pack...'; filterPacks(); }
        else if (tab === 'in1') { search.placeholder = 'Tìm tướng...'; filterIn1(); }
        else { search.placeholder = 'Tìm mod...'; filterCamxa(); }
    });
});

// ============ MOD LẺ DATA ============
const heroes = [
    { name: 'Nakroth', role: 'Sát Thủ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/c7b840bdacd7e5a8b83af72ccd9ca1815ec64fdc5ffeb1.jpg', skins: [
        { name: 'Thứ Nguyên Vệ Thần', quality: 'epic', url: 'https://link4m.com/QuyrVSs' },
        { name: 'Levi', quality: 'epic', url: 'https://link4m.net/yL0Khe' },
        { name: 'Bạch diện chiến thương', quality: 'epic', url: 'https://link4m.net/Qw8Zoi' },
        { name: 'Quy Thương Liệp Đế', quality: 'epic', url: 'https://link4m.net/RvjuA3h9' },
        { name: 'Killua', quality: 'epic', url: 'https://link4m.net/LKQ8Gp' },
    ]},
    { name: 'Florentino', role: 'Đấu Sĩ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/9527c1cbad1c0656d0a4adf1dcec38e35c25f62d77d671.jpg', skins: [
        { name: 'Kỷ nguyên hổ phách', quality: 'epic', url: 'https://link4m.com/SiDm4MD2' },
    ]},
    { name: 'Tulen', role: 'Pháp Sư', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/07210c9e529faa7766ba324bd86b75165a81722f3eab81.jpg', skins: [
        { name: 'Gojo', quality: 'epic', url: 'https://link4m.net/QdQLyw61' },
    ]},
    { name: 'Billow', role: 'Sát Thủ', img: 'https://lienquan.garena.vn/wp-content/uploads/2025/01/59900-2.jpg', skins: [
        { name: 'Thiên tướng - độ ách', quality: 'epic', url: 'https://link4m.com/pWJA5V' },
    ]},
    { name: 'Hayate', role: 'Xạ Thủ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/02c8e3d1db8ee8f32913b478884f33e05c8f254a7686f1.jpg', skins: [
        { name: 'Siêu đạo chích KID', quality: 'epic', url: 'https://link4m.com/fszCOtMD' },
    ]},
    { name: 'Paine', role: 'Sát Thủ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/47861c6d53d72d0dbea2d1dba0b0e0365e8ade6f180931.jpg', skins: [
        { name: 'Megumi Fushirugo', quality: 'epic', url: 'https://link4m.com/7B1dt9kx' },
    ]},
    { name: 'Cresht', role: 'Đỡ Đòn', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/04b0a1140d89b8ef0cd4a655753bbb895c4938662bc9f1.jpg', skins: [
        { name: 'Eren', quality: 'epic', url: 'https://link4m.com/AYzh4xG' },
    ]},
    { name: 'Lauriel', role: 'Pháp Sư', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/18d4327ac2e366a736a060be082bbbef5943917dab8d81.jpg', skins: [
        { name: 'Thứ Nguyên Vệ Thần', quality: 'epic', url: 'https://link4m.net/EJP2aFn3' },
    ]},
    { name: 'Yue', role: 'Pháp Sư', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/3ee26051086fee856dc6df74811e9e35658d4142ce14c1.jpg', skins: [
        { name: 'Hỗn Độn Thần Ma', quality: 'epic', url: 'https://link4m.com/aa6Mo' },
    ]},
    { name: 'Sinestrea', role: 'Sát Thủ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/680ef284724e077237f33cfc2d8fa72d5fa194bad60f31.jpg', skins: [
        { name: 'Wave', quality: 'epic', url: 'https://link4m.com/A7B0bkIu' },
    ]},
    { name: 'Qi', role: 'Đấu Sĩ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/6da178e8a2c2871aeb856bec0f669ccd5d5684e01acd31.jpg', skins: [
        { name: 'Milim Nava', quality: 'epic', url: 'https://link4m.com/FMRSCns' },
    ]},
];

// ============ MOD PACK DATA ============
const modPacks = [
    {
        name: 'Pack 47 Skin',
        img: 'https://cdn.phototourl.com/free/2026-06-14-f2d072ed-9482-4d03-b26b-d32fc568df1f.jpg',
        desc: 'Fix lag đầu game 99% Mở Khóa FPS 60/90/120/144 Load trận siêu nhanh HD hiệu ứng ngoại hình mọi cấu hình Cam Xa 5% Ko lỗi mạng .',
        url: 'https://link4m.org/niyMGu',
        skins: [''],
    },
    {
        name: 'Pack 112 Skin Liên Quân',
        img: 'https://cdn.phototourl.com/free/2026-06-15-3acf7968-f269-4ece-ba9d-5e45eb975083.jpg',
        desc: 'Mỗi tướng nhiều skin ,Ko bị reset, lỗi mạng, giật lag. Có gia tốc, biến về,cam xa, điệu nhảy, Fix lag 90%,Unlock FPS 60/90/120/144, Ko lỗi mạng, Điệu nhảy, Biến về, gia tốc, 1 tướng Mod nhiều skin √.',
        url: 'https://link4m.org/cucso',
        skins: [''],
    },
    {
        name: 'Pack 103 Skin Liên Quân',
        img: 'https://cdn.phototourl.com/free/2026-06-15-afaa0717-d25b-4d79-a9fd-3b3bb9d9ae15.jpg',
        desc: 'Mỗi tướng nhiều skin ,Ko bị reset, lỗi mạng, giật lag. Có gia tốc, biến về,cam xa, điệu nhảy, Fix lag 90%, Ko lỗi mạng, Điệu nhảy, Biến về, gia tốc, 1 tướng Mod nhiều skin √.',
        url: 'https://link4m.net/c5jF0zf',
        skins: [''],
    },
];

// ============ MOD SKIN IN1 DATA ============
const heroesIn1 = [
    { name: 'Tulen', role: 'Pháp Sư', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/07210c9e529faa7766ba324bd86b75165a81722f3eab81.jpg', url: 'https://link4m.net/wb2Jthw', desc: 'Tulen Mđ - Robot .Nhà thám hiểm - Chí tôn. Phù thủy kiến tạo - Bạch trạch. Dạ hội - Gojo.' },
    { name: 'Nakroth', role: 'Sát Thủ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/c7b840bdacd7e5a8b83af72ccd9ca1815ec64fdc5ffeb1.jpg', url: 'https://link4m.net/KLze5', desc: 'Mặc định - Bạch Diện Chiến Thương .Chiến Binh Hỏa Ngục - Killua .Quân Đoàn Địa Ngục - Thứ Nguyên Vệ Thần .Byboy Công Nghệ - Quỷ Thương Liệp Đế  .Quán quân - Lôi Quang Sứ .Producer Tia chớp - Levi có thông báo hạ .' },
    { name: 'Raz', role: 'Pháp Sư', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/6b79035779ab9195c76d91b3f2e7ca79591e6857831601.jpg', url: 'https://link4m.com/f0K6GbZn', desc: 'Mặc Định : Muay Thái, Đại Tù Trưởng : Bão Vũ Cuồng Lôi, Saitama : Gon.' },
    { name: 'Airi', role: 'Đấu Sĩ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/04999ff87145b9005694ffd78e1530a660017059a8fc11.jpg', url: 'https://link4m.net/Ysrpq7D', desc: 'Airi MĐ - Bích hải thánh nữ. Đặc công tử điệp - bạch Kimono .Quản lý tài năng - Thứ Nguyên Vệ Thần.' },
    { name: 'Florentino', role: 'Đấu Sĩ', img: 'https://lienquan.garena.vn/wp-content/uploads/2024/05/9527c1cbad1c0656d0a4adf1dcec38e35c25f62d77d671.jpg', url: 'https://link4m.net/xeUc8PH', desc: 'Mặc Định : Seven, Vũ Kiếm Sư : Bá Vương Âm Nhạc, Hy Lạp : Kỷ Nguyên Hổ Phách.' },
];

// ============ CAM XA & FPS DATA ============
const camxaMods = [
    {
        name: 'Cam Xa 5%-30% ',
        desc: 'Anh em in tâm nhé, đây là mod nên ko bị ban đâu.',
        url: 'https://link4m.net/eX1vagrQ',
        features: ['Quang sát map dễ hơn', 'Đây là Mod nên an toàn 100%', 'Không bị sập camera', 'Nhẹ, không lag']
    },
    {
        name: 'Cam Xa Mod Đè Lên File Mod Khác Được',
        desc: 'Chỉ Có Thể Mod Đè Lên File Mod Kênh Mình Thôi Nha (Kiana Mod AOV).',
        url: 'https://link4m.org/935D4u',
        features: ['Không bị mất biến về mod', 'Đây là Mod nên an toàn 100%', 'Không bị sập camera', 'Nhẹ, không lag']
    },
    {
        name: 'Cam Xa Tùy chỉnh',
        desc: 'Anh em in tâm nhé, đây là mod nên ko bị ban đâu.',
        url: 'https://link4m.net/581Bbc',
        features: ['Có thể tùy chỉnh độ xa ngay trong game bằng các ấn nút biến về', 'Đây là Mod nên an toàn 100%', 'Có thể bị sập camera đối vs các tướng có cam', 'Nhẹ, không lag']
    },
    {
        name: 'MỞ KHÓA FPS 60-90-120-144',
        desc: 'Có thể mod đè lên file mod.',
        url: 'https://link4m.net/i1xAs',
        features: ['Mở khóa FPS 60-90-120-144', 'Đây là Mod nên an toàn 100%', 'tốn pin', 'Nhẹ, mượt mà']
    },
];

// ============ CAM XA & FPS RENDER ============
function renderCamxa(filtered) {
    const grid = document.getElementById('grid-camxa');
    grid.innerHTML = filtered.map((mod, idx) => `
        <div class="camxa-card">
            <div class="camxa-header">
                <div class="camxa-icon">&#9881;</div>
                <h3>${mod.name}</h3>
            </div>
            <div class="camxa-desc">${mod.desc}</div>
            <div class="camxa-features">
                ${mod.features.map(f => `<span class="camxa-tag">${f}</span>`).join('')}
            </div>
            <div class="camxa-actions">
                <a href="${mod.url}" class="camxa-download" target="_blank">&#8595; Tải Xuống</a>
            </div>
        </div>
    `).join('');
    document.getElementById('count-camxa').textContent = filtered.length > 0 ? `${filtered.length} mod được tìm thấy` : '';
}

function filterCamxa() {
    const q = document.getElementById('searchInput').value.toLowerCase().trim();
    let f = camxaMods;
    if (q) f = f.filter(m => m.name.toLowerCase().includes(q) || m.desc.toLowerCase().includes(q) || m.features.some(f => f.toLowerCase().includes(q)));
    renderCamxa(f);
}

// ============ COMMON HELPERS ============
const qualityLabels = { common: 'Thường', rare: 'Hiếm', epic: 'Siêu Phẩm', legendary: 'Huyền Thoại' };
const roleClassMap = { 'Xạ Thủ': 'XạThủ', 'Pháp Sư': 'PhápSư', 'Đấu Sĩ': 'ĐấuSĩ', 'Sát Thủ': 'SátThủ', 'Đỡ Đòn': 'ĐỡĐòn', 'Hỗ Trợ': 'HỗTrợ' };
const roleColors = { 'Xạ Thủ': { from: '#dc3545', to: '#a71d2a' }, 'Pháp Sư': { from: '#6f42c1', to: '#4a248a' }, 'Đấu Sĩ': { from: '#fd7e14', to: '#c25d00' }, 'Sát Thủ': { from: '#28a745', to: '#1a7a32' }, 'Đỡ Đòn': { from: '#007bff', to: '#0056b3' }, 'Hỗ Trợ': { from: '#e83e8c', to: '#b11a6b' } };

function heroImg(name, role) {
    const hero = heroes.find(h => h.name === name) || heroesIn1.find(h => h.name === name);
    if (hero && hero.img) return hero.img;
    const initial = name.split("'")[0].charAt(0).toUpperCase();
    const c = roleColors[role] || { from: '#555', to: '#333' };
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:${c.from}"/><stop offset="100%" style="stop-color:${c.to}"/></linearGradient></defs><rect width="100" height="100" rx="50" fill="url(#bg)"/><circle cx="50" cy="50" r="42" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/><text x="50" y="50" text-anchor="middle" dominant-baseline="central" font-family="Inter,sans-serif" font-size="40" font-weight="700" fill="#fff">${initial}</text><path d="M0 50 Q25 30 50 50 T100 50" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/></svg>`;
    return 'data:image/svg+xml,' + encodeURIComponent(svg);
}

// ============ TAB 1: MOD LẺ ============
let modleRole = 'all';

function renderHeroes(filtered) {
    const grid = document.getElementById('grid-modle');
    const source = currentTab === 'modle' ? heroes : heroesIn1;
    grid.innerHTML = filtered.map((hero, idx) => `
        <div class="hero-card" onclick="openModleModal(${source.indexOf(hero)})">
            <div class="hero-avatar" style="background:none;border:none">
                <img src="${heroImg(hero.name, hero.role)}" alt="${hero.name}" class="avatar-img" loading="lazy">
            </div>
            <h3>${hero.name}</h3>
            <span class="hero-role ${roleClassMap[hero.role]}">${hero.role}</span>
            <div class="skin-count">${hero.skins.length} skin</div>
        </div>
    `).join('');
    document.getElementById('count-modle').textContent = filtered.length > 0 ? `${filtered.length} tướng được tìm thấy` : '';
}

function filterHeroes() {
    const q = document.getElementById('searchInput').value.toLowerCase().trim();
    let f = heroes;
    if (modleRole !== 'all') f = f.filter(h => h.role === modleRole);
    if (q) f = f.filter(h => h.name.toLowerCase().includes(q) || h.skins.some(s => s.name.toLowerCase().includes(q)));
    renderHeroes(f);
}

function filterByRole(role) {
    modleRole = role;
    const btns = document.querySelectorAll('#tab-modle .filter-btn');
    btns.forEach(b => b.classList.remove('active'));
    if (role === 'all') btns[0].classList.add('active');
    else [...btns].find(b => b.textContent === role)?.classList.add('active');
    filterHeroes();
}

function openModleModal(idx) {
    const hero = heroes[idx];
    const overlay = document.getElementById('modalOverlay');
    document.getElementById('modalContent').innerHTML = `
        <div class="modal-header">
            <img src="${heroImg(hero.name, hero.role)}" alt="${hero.name}" class="modal-avatar-img">
            <h2>${hero.name}</h2>
            <span class="hero-role ${roleClassMap[hero.role]}">${hero.role}</span>
        </div>
        <div class="skin-list">
            ${hero.skins.map(s => `
                <div class="skin-item">
                    <div class="skin-info">
                        <span class="skin-name">${s.name}</span>
                        <span class="skin-quality ${s.quality}">${qualityLabels[s.quality]}</span>
                    </div>
                    <a href="${s.url}" class="download-btn" target="_blank">&#8595; Tải</a>
                </div>
            `).join('')}
        </div>
    `;
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// ============ TAB 2: MOD PACK ============
let packSearch = '';

function renderPacks(filtered) {
    const grid = document.getElementById('grid-modpack');
    grid.innerHTML = filtered.map(p => `
        <div class="pack-card">
            <img src="${p.img}" alt="${p.name}" class="pack-img" loading="lazy" onerror="this.src='${heroImg(p.name, '')}'">
            <div class="pack-body">
                <h3>${p.name}</h3>
                <div class="pack-desc">${p.desc}</div>
                <div class="pack-skins">
                    <h4>Danh sách skin trong pack</h4>
                    ${p.skins.map(s => `<span class="pack-skin-tag">${s}</span>`).join('')}
                </div>
                <a href="${p.url}" class="pack-download" target="_blank">&#8595; Tải Xuống</a>
            </div>
        </div>
    `).join('');
    document.getElementById('count-modpack').textContent = filtered.length > 0 ? `${filtered.length} pack được tìm thấy` : '';
}

function filterPacks() {
    const q = document.getElementById('searchInput').value.toLowerCase().trim();
    let f = modPacks;
    if (q) f = f.filter(p => p.name.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q) || p.skins.some(s => s.toLowerCase().includes(q)));
    renderPacks(f);
}

// ============ TAB 3: MOD SKIN IN1 ============
let in1Role = 'all';

function renderIn1(filtered) {
    const grid = document.getElementById('grid-in1');
    grid.innerHTML = filtered.map((hero, idx) => `
        <div class="hero-card" onclick="openIn1Modal(${heroesIn1.indexOf(hero)})">
            <div class="hero-avatar" style="background:none;border:none">
                <img src="${heroImg(hero.name, hero.role)}" alt="${hero.name}" class="avatar-img" loading="lazy">
            </div>
            <h3>${hero.name}</h3>
            <span class="hero-role ${roleClassMap[hero.role]}">${hero.role}</span>
            <div class="skin-count">1 link tải</div>
        </div>
    `).join('');
    document.getElementById('count-in1').textContent = filtered.length > 0 ? `${filtered.length} tướng được tìm thấy` : '';
}

function filterIn1() {
    const q = document.getElementById('searchInput').value.toLowerCase().trim();
    let f = heroesIn1;
    if (in1Role !== 'all') f = f.filter(h => h.role === in1Role);
    if (q) f = f.filter(h => h.name.toLowerCase().includes(q) || h.desc.toLowerCase().includes(q));
    renderIn1(f);
}

function filterIn1Role(role) {
    in1Role = role;
    const btns = document.querySelectorAll('#tab-in1 .filter-btn');
    btns.forEach(b => b.classList.remove('active'));
    if (role === 'all') btns[0].classList.add('active');
    else [...btns].find(b => b.textContent === role)?.classList.add('active');
    filterIn1();
}

function openIn1Modal(idx) {
    const hero = heroesIn1[idx];
    const overlay = document.getElementById('modalOverlay');
    document.getElementById('modalContent').innerHTML = `
        <div class="modal-header">
            <img src="${heroImg(hero.name, hero.role)}" alt="${hero.name}" class="modal-avatar-img">
            <h2>${hero.name}</h2>
            <span class="hero-role ${roleClassMap[hero.role]}">${hero.role}</span>
        </div>
        <div class="modal-desc">${hero.desc}</div>
        <a href="${hero.url}" class="modal-download-btn" target="_blank">&#8595; Tải Mod Skin ${hero.name}</a>
    `;
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// ============ SEARCH GLOBAL ============
document.getElementById('searchInput').addEventListener('input', () => {
    if (currentTab === 'modle') filterHeroes();
    else if (currentTab === 'modpack') filterPacks();
    else if (currentTab === 'in1') filterIn1();
    else filterCamxa();
});

// ============ GUIDE MODAL ============
function openGuide() {
    document.getElementById('guideContent').innerHTML = `
        <div class="modal-header">
            <h2 style="font-size:22px">&#9654; Hướng dẫn cài mod skin</h2>
        </div>
        <div class="guide-video-wrap">
            <iframe src="https://www.youtube.com/embed/B8z_nrCqJL0" allowfullscreen></iframe>
        </div>
        <div class="guide-links">
            <div class="guide-link-item">
                <span class="label">Resources</span>
                <span class="link-val" id="linkResources">https://tinyurl.com/Resources-KianaMod</span>
                <button class="copy-btn" onclick="copyLink('linkResources')">Sao chép</button>
            </div>
            <div class="guide-link-item">
                <span class="label">MT Manager</span>
                <span class="link-val" id="linkMT">https://mt-manager.net/download/</span>
                <button class="copy-btn" onclick="copyLink('linkMT')">Sao chép</button>
            </div>
        </div>
        <div class="guide-note">
            <strong>&#9432; Lưu ý:</strong> Xem video hướng dẫn ở trên để biết cách cài mod chi tiết.
            Sau khi tải file mod về, dùng <strong>MT Manager</strong> để giải nén và thay thế file trong thư mục game.
        </div>
    `;
    document.getElementById('guideOverlay').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeGuide() {
    document.getElementById('guideOverlay').classList.remove('active');
    document.body.style.overflow = '';
}

function copyLink(id) {
    const text = document.getElementById(id).textContent;
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.querySelector(`#${id}`).nextElementSibling;
        const orig = btn.textContent;
        btn.textContent = '&#10003; Đã copy';
        btn.style.borderColor = '#28a745';
        btn.style.color = '#28a745';
        setTimeout(() => {
            btn.textContent = orig;
            btn.style.borderColor = '';
            btn.style.color = '';
        }, 2000);
    });
}

// ============ MODAL ============
document.getElementById('modalOverlay').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) closeModal();
});
document.getElementById('guideOverlay').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) closeGuide();
});

function closeModal() {
    document.getElementById('modalOverlay').classList.remove('active');
    document.body.style.overflow = '';
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { closeModal(); closeGuide(); }
});

// ============ MUSIC ============
function toggleMusic() {
    const audio = document.getElementById('bgMusic');
    const btn = document.getElementById('musicBtn');
    if (audio.paused) {
        audio.play();
        btn.classList.add('playing');
        btn.textContent = '&#9834;';
    } else {
        audio.pause();
        btn.classList.remove('playing');
        btn.textContent = '&#9835;';
    }
}

// ============ INIT ============
renderHeroes(heroes);
