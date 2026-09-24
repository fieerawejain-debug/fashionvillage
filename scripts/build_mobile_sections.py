import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the temporary mobile snippets added earlier so we can place complete, clean sections
if 'class="mobile-hero-spotlight"' in html:
    # clean out the old mobile hero spotlight
    s_idx = html.find('<!-- Mobile Hero Quick-Actions & Spotlight Card -->')
    if s_idx != -1:
        e_idx = html.find('</div>\n    </div>', s_idx)
        if e_idx != -1:
            html = html[:s_idx] + html[e_idx + len('</div>\n    </div>'):]

if 'class="mobile-concierge-actions"' in html:
    s_idx = html.find('<!-- Mobile Concierge Action Buttons -->')
    if s_idx != -1:
        e_idx = html.find('</div>', s_idx)
        if e_idx != -1:
            html = html[:s_idx] + html[e_idx + len('</div>'):]

# 1. Section 1 (Hero)
hero_desktop_target = '<section class="section-bleed bleed-hero" id="hero" aria-labelledby="hero-title">\n    <div class="section-frame">'
hero_desktop_replacement = '''<section class="section-bleed bleed-hero" id="hero" aria-labelledby="hero-title">
    <div class="section-frame desktop-only">'''

mobile_hero_block = '''
    <!-- Mobile Hero Section (Dedicated Luxury Touch UI) -->
    <div class="mobile-only mobile-hero-container">
      <div class="mobile-hero-banner">
        <img src="assets/hero_trimmed.png" alt="Heritage Woven in Silk & Gold - 2025 Sovereign Edit">
      </div>
      <div class="mobile-hero-content">
        <div class="mobile-hero-title-box">
          <span class="mobile-hero-sub">2025 SOVEREIGN EDIT</span>
          <h1 class="mobile-hero-h1">Heritage Woven in Silk &amp; Gold</h1>
        </div>
        <div class="mobile-quick-actions">
          <a href="#categories" class="mobile-action-pill">
            <span>✨</span> 420+ Silks
          </a>
          <button type="button" class="mobile-action-pill trigger-appointment">
            <span>📅</span> Video Salon
          </button>
          <button type="button" class="mobile-action-pill trigger-whatsapp">
            <span>💬</span> WhatsApp
          </button>
        </div>
        <div class="mobile-product-card">
          <div class="mobile-product-tag">Bridal Heirlooms • 2025 Sovereign Edit</div>
          <div class="mobile-product-title">The Rudraksha Mayil Kanchipuram</div>
          <div class="mobile-product-pricing">
            <span style="font-size:18px; font-weight:700; color:#201817;" data-inr-price="48500">₹48,500</span>
            <span style="font-size:13px; color:#9E8F8B; text-decoration:line-through;" data-inr-price="58000">₹58,000</span>
            <span style="font-size:10px; background:#FEF3C7; color:#92400E; font-weight:700; padding:2px 6px; border-radius:3px;">Handloom Mark</span>
          </div>
          <button type="button" class="mobile-product-btn" onclick="openProductQuickView('The Rudraksha Mayil Kanchipuram', 48500, 'Hand-spun on a traditional triple-shuttle Korvai pit-loom. Sacred Rudraksha motifs and twin Mayil medallions along the authentic Ganga-Jamuni border.')">
            Quick View Saree &amp; Tested Zari &rarr;
          </button>
        </div>
      </div>
    </div>
'''

if hero_desktop_target in html:
    html = html.replace(hero_desktop_target, hero_desktop_replacement)
    # Insert mobile hero right before </section>
    hero_end = '</section>\n\n  <!-- =========================================================================\n       3. Interactive Concierge Banner'
    html = html.replace(hero_end, mobile_hero_block + '  ' + hero_end)

# 2. Section 2 (Concierge)
concierge_desktop_target = '<section class="section-bleed bleed-concierge" id="concierge" aria-labelledby="concierge-title">\n    <div class="section-frame">'
concierge_desktop_replacement = '''<section class="section-bleed bleed-concierge" id="concierge" aria-labelledby="concierge-title">
    <div class="section-frame desktop-only">'''

mobile_concierge_block = '''
    <!-- Mobile Concierge Suite -->
    <div class="mobile-only mobile-section mobile-concierge-suite">
      <div class="mobile-concierge-card">
        <div class="concierge-crown">👑</div>
        <span class="mobile-section-sub" style="color:var(--color-gold-light);">SOVEREIGN TROUSSEAU CONCIERGE</span>
        <h2 class="mobile-section-title" style="color:#FFF; margin: 6px 0 10px;">Private 4K Video Styling Suite</h2>
        <p style="font-size:12.5px; color:#E8DFDC; line-height:1.6; margin-bottom:18px;">
          Experience bespoke private video trials with senior master curators. Live high-definition draping broadcasts directly from our Chennai and Varanasi loom ateliers.
        </p>
        <div class="mobile-concierge-btns-stack">
          <button type="button" class="btn-submit trigger-appointment" style="width:100%; text-align:center;">
            📅 BOOK COMPLIMENTARY VIDEO APPOINTMENT
          </button>
          <button type="button" class="btn-submit trigger-whatsapp" style="width:100%; text-align:center; background:#25D366; color:#FFF;">
            💬 CHAT WITH SENIOR STYLIST ON WHATSAPP
          </button>
        </div>
      </div>
    </div>
'''

if concierge_desktop_target in html:
    html = html.replace(concierge_desktop_target, concierge_desktop_replacement)
    concierge_end = '</section>\n\n  <!-- =========================================================================\n       4. Section 3: Category Showcase Grid'
    html = html.replace(concierge_end, mobile_concierge_block + '  ' + concierge_end)

# 3. Section 3 (Categories)
cat_target = '<section class="section-bleed bleed-categories" id="categories" aria-labelledby="cat-heading">\n    <div class="section-frame">'
cat_replacement = '''<section class="section-bleed bleed-categories" id="categories" aria-labelledby="cat-heading">
    <div class="section-frame desktop-only">'''

mobile_cat_block = '''
    <!-- Mobile Category Showcase Grid (High-Res 2x2 Grid) -->
    <div class="mobile-only mobile-section mobile-categories-section">
      <div class="mobile-section-header">
        <span class="mobile-section-sub">SIGNATURE CURATIONS</span>
        <h2 class="mobile-section-title">Pillars of Indian Drapes</h2>
      </div>
      <div class="mobile-categories-grid">
        <a href="kanjivaram.html" class="mobile-cat-card">
          <img src="assets/mobile/cat_kanjivaram.png" alt="Pure Kanjivaram & Temple Silks">
        </a>
        <a href="banarasi.html" class="mobile-cat-card">
          <img src="assets/mobile/cat_banarasi.png" alt="Banarasi Zari Elegance">
        </a>
        <a href="everyday.html" class="mobile-cat-card">
          <img src="assets/mobile/cat_everyday.png" alt="Everyday & Office Wear">
        </a>
        <a href="kanjivaram.html" class="mobile-cat-card">
          <img src="assets/mobile/cat_festive.png" alt="Festive & Celebration Drapes">
        </a>
      </div>
    </div>
'''

if cat_target in html:
    html = html.replace(cat_target, cat_replacement)
    cat_end = '</section>\n\n  <!-- =========================================================================\n       5. Section 4: Curated Bestsellers Section'
    html = html.replace(cat_end, mobile_cat_block + '  ' + cat_end)

# 4. Section 4 (Curated Bestsellers)
best_target = '<section class="section-bleed bleed-bestsellers" id="bestsellers" aria-labelledby="bestsellers-heading">\n    <div class="section-frame">'
best_replacement = '''<section class="section-bleed bleed-bestsellers" id="bestsellers" aria-labelledby="bestsellers-heading">
    <div class="section-frame desktop-only">'''

mobile_best_block = '''
    <!-- Mobile Curated Bestsellers Grid (Tap-to-Quick-View) -->
    <div class="mobile-only mobile-section mobile-bestsellers-section">
      <div class="mobile-section-header">
        <span class="mobile-section-sub">HIGH DEMAND WEAVES</span>
        <h2 class="mobile-section-title">Curated Bestsellers</h2>
      </div>
      <div class="mobile-bestsellers-grid">
        <div class="mobile-best-card" onclick="openProductQuickView('Maharani Crimson Gold Mayil Saree', 34800, 'Pure Mulberry Silk with Tested Zari Weft. Hand-spun in Kanchipuram.')">
          <img src="assets/mobile/best_1.png" alt="Maharani Crimson Gold Mayil Saree">
        </div>
        <div class="mobile-best-card" onclick="openProductQuickView('Banarasi Katan Shikargah', 58500, 'Pure Silver Weft, Consecrated Mulberry Silk.')">
          <img src="assets/mobile/best_2.png" alt="Banarasi Katan Shikargah">
        </div>
        <div class="mobile-best-card" onclick="openProductQuickView('Tissue Organza Bridal Draping', 34500, 'Featherlight Metallic Sheen in Champagne Gold.')">
          <img src="assets/mobile/best_3.png" alt="Tissue Organza Bridal Draping">
        </div>
        <div class="mobile-best-card" onclick="openProductQuickView('Arundhati Korvai Muhurtham Silk', 64000, 'Triple Shuttle Pit Loom with Heritage Mayil Border.')">
          <img src="assets/mobile/best_4.png" alt="Arundhati Korvai Muhurtham Silk">
        </div>
      </div>
    </div>
'''

if best_target in html:
    html = html.replace(best_target, best_replacement)
    best_end = '</section>\n\n  <!-- =========================================================================\n       6. Section 5: \'Everyday Grace\''
    html = html.replace(best_end, mobile_best_block + '  ' + best_end)

# 5. Section 5 (Everyday Grace)
everyday_target = '<section class="section-bleed bleed-everyday" id="everyday-grace" aria-labelledby="everyday-heading">\n    <div class="section-frame">'
everyday_replacement = '''<section class="section-bleed bleed-everyday" id="everyday-grace" aria-labelledby="everyday-heading">
    <div class="section-frame desktop-only">'''

mobile_everyday_block = '''
    <!-- Mobile Everyday Grace Spotlight -->
    <div class="mobile-only mobile-section mobile-everyday-section">
      <div class="mobile-section-header">
        <span class="mobile-section-sub">REGULAR WEAR SPOTLIGHT</span>
        <h2 class="mobile-section-title">Everyday Grace</h2>
      </div>
      <div class="mobile-everyday-card">
        <img src="assets/mobile/everyday_1.png" alt="Everyday Grace Mulmul & Linen">
      </div>
      <div class="mobile-everyday-card" style="margin-top:12px;">
        <img src="assets/mobile/everyday_2.png" alt="Office Luxe Silk-Linen Co-ords">
      </div>
      <div style="margin-top:16px;">
        <a href="everyday.html" class="btn-submit" style="width:100%; text-align:center; display:block;">
          EXPLORE EVERYDAY GRACE COLLECTION &rarr;
        </a>
      </div>
    </div>
'''

if everyday_target in html:
    html = html.replace(everyday_target, everyday_replacement)
    everyday_end = '</section>\n\n  <!-- =========================================================================\n       7. Section 6: The Craftsmanship'
    html = html.replace(everyday_end, mobile_everyday_block + '  ' + everyday_end)

# 6. Section 6 (Weaver Story)
story_target = '<section class="section-bleed bleed-craft" id="craftsmanship" aria-labelledby="craft-heading">\n    <div class="section-frame">'
story_replacement = '''<section class="section-bleed bleed-craft" id="craftsmanship" aria-labelledby="craft-heading">
    <div class="section-frame desktop-only">'''

mobile_story_block = '''
    <!-- Mobile Weaver Story Section -->
    <div class="mobile-only mobile-section mobile-story-section">
      <div class="mobile-section-header">
        <span class="mobile-section-sub">PRESERVING LIVING TRADITIONS</span>
        <h2 class="mobile-section-title">The Master Weaver Guild</h2>
      </div>
      <div class="mobile-story-card">
        <img src="assets/mobile/cat_festive.png" style="width:100%; height:200px; object-fit:cover; border-radius:6px;" alt="Master Handloom Weaver Guild">
        <p style="font-size:13.5px; color:#5D4E4A; line-height:1.7; margin:16px 0;">
          For over 45 generational years, Fashion Village has protected the sacred Korvai three-shuttle pit looms and pure silver zari assays. Every saree represents between 180 and 320 master artisan handloom hours.
        </p>
        <div style="display:flex; flex-direction:column; gap:10px;">
          <button type="button" class="btn-submit" onclick="openVideoLoomModal()" style="width:100%;">
            ▶ WATCH MASTER LOOM FILM (4 MIN)
          </button>
          <a href="story.html" class="btn-submit" style="width:100%; text-align:center; background:#FAF8F5; color:#63000D; border:1px solid #63000D;">
            READ WEAVER GUILD ARCHIVES &rarr;
          </a>
        </div>
      </div>
    </div>
'''

if story_target in html:
    html = html.replace(story_target, story_replacement)
    story_end = '</section>\n\n  <!-- =========================================================================\n       8. Section 7: Customer Testimonials'
    html = html.replace(story_end, mobile_story_block + '  ' + story_end)

# 7. Section 7 (Testimonials)
testimonials_target = '<section class="section-bleed bleed-testimonials" id="testimonials" aria-labelledby="testimonials-heading">\n    <div class="section-frame">'
testimonials_replacement = '''<section class="section-bleed bleed-testimonials" id="testimonials" aria-labelledby="testimonials-heading">
    <div class="section-frame desktop-only">'''

mobile_testimonials_block = '''
    <!-- Mobile Testimonials Section -->
    <div class="mobile-only mobile-section mobile-testimonials-section">
      <div class="mobile-section-header">
        <span class="mobile-section-sub">HONORED PATRONS & PRESS</span>
        <h2 class="mobile-section-title">Voices of Sovereignty</h2>
      </div>
      <div class="mobile-testimonial-card">
        <div style="color:var(--color-gold-deep); font-size:15px; margin-bottom:8px;">★★★★★</div>
        <p style="font-size:13.5px; font-style:italic; color:#3D3230; line-height:1.6; margin-bottom:10px;">
          &ldquo;The Rudraksha Mayil Kanchipuram arrived in London for my wedding within 3 days. The tested zari sheen and weight were breathtaking. It felt like wearing a piece of living heritage.&rdquo;
        </p>
        <div style="font-size:12px; font-weight:700; color:var(--color-maroon);">— Radhika Swaminathan, London (Verified Bride)</div>
      </div>
      <div class="mobile-testimonial-card" style="margin-top:12px;">
        <div style="color:var(--color-gold-deep); font-size:15px; margin-bottom:8px;">★★★★★</div>
        <p style="font-size:13.5px; font-style:italic; color:#3D3230; line-height:1.6; margin-bottom:10px;">
          &ldquo;Fashion Village sets the gold benchmark for tested zari transparency and authentic pit loom weaves.&rdquo;
        </p>
        <div style="font-size:12px; font-weight:700; color:var(--color-gold-deep);">— Architectural Digest Luxury Review</div>
      </div>
    </div>
'''

if testimonials_target in html:
    html = html.replace(testimonials_target, testimonials_replacement)
    testimonials_end = '</section>\n\n  <!-- =========================================================================\n       9. Section 8: Instagram Luxury Lookbook'
    html = html.replace(testimonials_end, mobile_testimonials_block + '  ' + testimonials_end)

# 8. Section 8 (Instagram Lookbook)
insta_target = '<section class="section-bleed bleed-instagram" id="lookbook" aria-labelledby="instagram-heading">\n    <div class="section-frame">'
insta_replacement = '''<section class="section-bleed bleed-instagram" id="lookbook" aria-labelledby="instagram-heading">
    <div class="section-frame desktop-only">'''

mobile_insta_block = '''
    <!-- Mobile Instagram Lookbook Gallery -->
    <div class="mobile-only mobile-section mobile-insta-section">
      <div class="mobile-section-header">
        <span class="mobile-section-sub">THE LIVING EDIT</span>
        <h2 class="mobile-section-title">@FashionVillageSilks</h2>
      </div>
      <div class="mobile-insta-grid">
        <div class="mobile-insta-item"><img src="assets/mobile/insta_1.png" alt="Instagram Lookbook 1"></div>
        <div class="mobile-insta-item"><img src="assets/mobile/insta_2.png" alt="Instagram Lookbook 2"></div>
        <div class="mobile-insta-item"><img src="assets/mobile/insta_3.png" alt="Instagram Lookbook 3"></div>
        <div class="mobile-insta-item"><img src="assets/mobile/insta_4.png" alt="Instagram Lookbook 4"></div>
      </div>
      <div style="text-align:center; margin-top:14px;">
        <a href="#" onclick="showToast('Follow @FashionVillageSilks on Instagram')" style="font-size:12px; font-weight:700; color:var(--color-maroon); letter-spacing:1px; text-transform:uppercase;">
          FOLLOW ON INSTAGRAM &rarr;
        </a>
      </div>
    </div>
'''

if insta_target in html:
    html = html.replace(insta_target, insta_replacement)
    insta_end = '</section>\n\n  <!-- =========================================================================\n       10. Fully Coded Luxury Responsive Footer'
    html = html.replace(insta_end, mobile_insta_block + '  ' + insta_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Index.html successfully upgraded with full mobile responsive architecture!')
