import os

index_path = 'index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update hotspot product trigger bounds
html = html.replace('left: 55.5%; top: 70.7%; width: 27.5%; height: 14.5%;', 'left: 53.5%; top: 70.9%; width: 29.5%; height: 13.7%;')

# 2. Add Mobile Search Toggle in header actions if not present
if 'id="mobile-search-toggle"' not in html:
    search_toggle_btn = '''        <!-- Mobile Search Toggle Button -->
        <button type="button" class="icon-action-btn mobile-search-toggle-btn" id="mobile-search-toggle" title="Search Weaves">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>
'''
    html = html.replace('<div class="header-nav-actions">', '<div class="header-nav-actions">\n' + search_toggle_btn)

# 3. Add Mobile Expandable Search Bar right after header if not present
if 'id="mobile-search-bar"' not in html:
    mobile_search = '''  <!-- Mobile Expandable Search Bar -->
  <div class="mobile-search-bar" id="mobile-search-bar">
    <div class="search-bar">
      <span class="search-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
      </span>
      <input type="text" id="mobile-search-input" class="search-input" placeholder="Search Kanjivaram, Banarasi, Zari...">
    </div>
  </div>
'''
    html = html.replace('</header>', '</header>\n\n' + mobile_search)

# 4. Add Mobile Hero Spotlight Card inside section-bleed bleed-hero right below section-frame
if 'class="mobile-hero-spotlight"' not in html:
    mobile_hero = '''
    <!-- Mobile Hero Quick-Actions & Spotlight Card -->
    <div class="mobile-hero-spotlight">
      <div class="mobile-quick-actions">
        <a href="#categories" class="mobile-action-pill">
          <span>✨</span> 420+ Royal Silks
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
        <button type="button" class="mobile-product-btn" onclick="openProductQuickView('The Rudraksha Mayil Kanchipuram', 48500, 'Hand-spun on a traditional triple-shuttle Korvai pit-loom. Sacred Rudraksha motifs and twin Mayil medallions.')">
          Quick View Saree &amp; Tested Zari &rarr;
        </button>
      </div>
    </div>
'''
    hero_end_marker = '</section>\n\n  <!-- =========================================================================\n       3. Interactive Concierge Banner'
    if hero_end_marker in html:
        html = html.replace(hero_end_marker, mobile_hero + '  </section>\n\n  <!-- =========================================================================\n       3. Interactive Concierge Banner')

# 5. Add Mobile Concierge Action Buttons inside section-bleed bleed-concierge
if 'class="mobile-concierge-actions"' not in html:
    mobile_concierge = '''
    <!-- Mobile Concierge Action Buttons -->
    <div class="mobile-concierge-actions">
      <button type="button" class="mobile-concierge-btn btn-video-mobile trigger-appointment">
        <span>📅</span> Book Private 4K Video Appointment
      </button>
      <button type="button" class="mobile-concierge-btn btn-wa-mobile trigger-whatsapp">
        <span>💬</span> Chat with Senior Loom Stylist on WhatsApp
      </button>
    </div>
'''
    concierge_end_marker = '</section>\n\n  <!-- =========================================================================\n       4. Section 3: Category Showcase Grid'
    if concierge_end_marker in html:
        html = html.replace(concierge_end_marker, mobile_concierge + '  </section>\n\n  <!-- =========================================================================\n       4. Section 3: Category Showcase Grid')

# 6. Replace Footer with the light luxury cream Figma-accurate footer
footer_start = '<footer class="luxury-footer" id="site-footer">'
footer_end = '</footer>'
f_start_idx = html.find(footer_start)
f_end_idx = html.find(footer_end, f_start_idx)

if f_start_idx != -1 and f_end_idx != -1:
    new_footer = '''<footer class="luxury-footer" id="site-footer">
    
    <!-- Main Footer 4 Columns -->
    <div class="footer-main">
      
      <!-- Brand & Craftsmanship Column -->
      <div class="footer-brand-col">
        <div class="footer-brand-title">FASHION VILLAGE</div>
        <div class="footer-brand-tagline">SILKS &amp; SAREES</div>
        <p class="footer-brand-desc">
          Handcrafted authenticity woven with generational mastery. Fashion Village honors South Asian loom traditions, bringing the world genuine bridal weaves, pure golden zari artistry, and bespoke regal ensembles.
        </p>

        <!-- Trust Badges (Silk Mark & Handloom Support) -->
        <div class="footer-badges-row">
          <div class="footer-trust-badge" title="Certified Pure Silk by Silk Mark Organization of India">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
            </svg>
            <span>Silk Mark Certified</span>
          </div>
          <div class="footer-trust-badge" title="100% Direct Master Weaver Guild Empowerment">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 22v-9"></path>
              <path d="M9 10a5 5 0 0 1 6 0"></path>
              <path d="M12 13a4 4 0 0 0 4-4 4 4 0 0 0-8 0 4 4 0 0 0 4 4z"></path>
              <path d="M12 3a9 9 0 0 0-9 9c0 3.5 2 6.5 5 8"></path>
              <path d="M12 3a9 9 0 0 1 9 9c0 3.5-2 6.5-5 8"></path>
            </svg>
            <span>100% Handloom Support</span>
          </div>
        </div>

        <!-- Social Channels -->
        <div class="footer-social-row">
          <a href="#" class="footer-social-icon" title="Instagram @FashionVillageSilks" onclick="showToast('Follow @FashionVillageSilks on Instagram')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </a>
          <a href="#" class="footer-social-icon" title="Pinterest Lookbooks" onclick="showToast('Explore our Lookbooks on Pinterest')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0a12 12 0 0 0-4.37 23.18c-.06-.99-.1-2.52.02-3.61l.73-3.11s-.18-.37-.18-.92c0-.86.5-1.5 1.12-1.5.53 0 .78.4.78.88 0 .53-.34 1.33-.51 2.07-.15.61.3 1.11.9 1.11 1.08 0 1.91-1.14 1.91-2.79 0-1.46-1.05-2.48-2.55-2.48-1.74 0-2.76 1.3-2.76 2.65 0 .52.2 1.08.45 1.39.05.06.06.12.04.18l-.17.69c-.03.11-.1.15-.22.1-1.02-.47-1.66-1.95-1.66-3.14 0-2.56 1.86-4.91 5.36-4.91 2.81 0 5 2 5 4.69 0 2.8-1.76 5.05-4.21 5.05-.82 0-1.6-.43-1.86-.94l-.51 1.94c-.18.71-.68 1.6-1.01 2.15A11.99 11.99 0 0 0 12 24c6.63 0 12-5.37 12-12S18.63 0 12 0z"/>
            </svg>
          </a>
          <a href="#" class="footer-social-icon" title="WhatsApp Concierge" onclick="openDrawer(document.getElementById('whatsapp-drawer'))">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.077-2.008-.466-1.579-.654-2.597-2.261-2.677-2.367-.077-.105-.635-.847-.635-1.616 0-.769.404-1.148.547-1.306.144-.158.314-.198.418-.198.106 0 .211.002.304.006.098.005.23-.037.36.275.134.321.458 1.116.498 1.198.04.081.067.176.013.282-.053.107-.08.175-.16.269-.08.093-.169.208-.241.279-.08.079-.164.165-.07.327.093.162.417.689.896 1.115.616.549 1.135.719 1.298.8.162.081.258.07.354-.041.096-.111.411-.479.521-.643.111-.164.22-.137.37-.082.15.054.957.451 1.121.533.164.082.274.122.314.19.04.068.04.394-.104.799z"/>
            </svg>
          </a>
        </div>
      </div>

      <!-- Column 2: The Collections -->
      <div>
        <div class="footer-col-title">The Collections</div>
        <ul class="footer-links-list">
          <li><a href="kanjivaram.html">Kanchipuram Silks</a></li>
          <li><a href="banarasi.html">Banarasi Brocades</a></li>
          <li><a href="everyday.html">Chanderi &amp; Tussar</a></li>
          <li><a href="banarasi.html">Organza &amp; Tissue Drapes</a></li>
          <li><a href="kanjivaram.html">Heritage Bridal Lehengas</a></li>
          <li><a href="everyday.html">Handcrafted Daily Kurtas</a></li>
        </ul>
      </div>

      <!-- Column 3: Client Concierge -->
      <div>
        <div class="footer-col-title">Client Concierge</div>
        <ul class="footer-links-list">
          <li><a href="#" onclick="openModal(document.getElementById('store-modal'))">Palace Store Locator</a></li>
          <li><a href="#" onclick="openModal(document.getElementById('appointment-modal'))">Book a Bridal Stylist</a></li>
          <li><a href="#" onclick="showToast('Complimentary insured global express shipping on all pure silks.')">Complimentary Global Express</a></li>
          <li><a href="#" onclick="showToast('Every saree carries certified 100% Tested Silver-Gilt Zari Assay.')">Zari Quality Certification</a></li>
          <li><a href="#" onclick="showToast('Bespoke pico, fall edging and pure silk blouse customization included.')">Fall, Pico &amp; Blouse Tailoring</a></li>
          <li><a href="#" onclick="showToast('Bespoke bridal trousseau tracking active for VIP consignments.')">Track Bespoke Consignment</a></li>
        </ul>
      </div>

      <!-- Column 4: Private VIP Salon -->
      <div>
        <div class="footer-col-title">Private VIP Salon</div>
        <p class="vip-salon-desc">
          Receive sovereign invitations to heirloom trunk shows, bridal trousseau launches, and artisanal previews.
        </p>
        <form class="vip-salon-form" onsubmit="event.preventDefault(); subscribeNewsletter();">
          <input type="email" id="newsletter-email" class="vip-salon-input" placeholder="Enter your VIP email..." required>
          <button type="submit" class="vip-salon-btn">JOIN</button>
        </form>
        <div class="vip-salon-note">STRICT PRIVACY. CURATED ROYAL EDITS ONLY.</div>
      </div>

    </div>

    <!-- Bottom Copyright & Policy Links -->
    <div class="footer-bottom-bar">
      <div class="footer-bottom-inner">
        <div>&copy; 2025 Fashion Village Silks &amp; Sarees Private Limited. All Rights Reserved.</div>
        <div class="footer-bottom-links">
          <a href="#" onclick="showToast('Silk Mark Protocol: Verified Pure Natural Mulberry Silk')">SILK MARK PROTOCOL</a>
          <span>&bull;</span>
          <a href="#" onclick="showToast('Terms of Heritage Sale: Generational Guild Authenticity Guarantee')">TERMS OF HERITAGE SALE</a>
          <span>&bull;</span>
          <a href="#" onclick="showToast('Worldwide Insured Express Delivery via DHL Luxury Express')">WORLDWIDE INSURED SHIPPING</a>
        </div>
        <div class="footer-secure-tag">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
          </svg>
          <span>ENCRYPTED LUXURY GATEWAY</span>
        </div>
      </div>
    </div>

  </footer>'''
    html = html[:f_start_idx] + new_footer + html[f_end_idx + len(footer_end):]

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Index.html successfully updated with all mobile enhancements and luxury cream footer!')
