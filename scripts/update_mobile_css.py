import os

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure .desktop-only and .mobile-only are defined cleanly
mobile_css_additions = '''
/* --------------------------------------------------------------------------
   Mobile-First Adaptive Display & Component Architecture
   -------------------------------------------------------------------------- */
.mobile-only {
  display: none !important;
}

.desktop-only {
  display: block;
}

@media (max-width: 768px) {
  .desktop-only {
    display: none !important;
  }

  .mobile-only {
    display: block !important;
  }

  /* Sticky Mobile Header */
  .top-announcement-bar {
    height: auto;
    padding: 7px 12px;
  }

  .announcement-text {
    font-size: 9.5px;
    letter-spacing: 0.5px;
    white-space: normal;
    text-align: center;
    line-height: 1.35;
  }

  .announcement-text .dot {
    display: none;
  }

  .header-container {
    height: 58px;
    padding: 0 12px;
    gap: 8px;
  }

  .brand-name {
    font-size: 17px;
    letter-spacing: 0.5px;
    line-height: 1;
  }

  .brand-sub {
    font-size: 6.5px;
    letter-spacing: 1px;
    margin-top: 2px;
  }

  .search-container {
    display: none;
  }

  .mobile-menu-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    flex-shrink: 0;
  }

  #store-locator-btn,
  .header-v-divider,
  #currency-selector-btn,
  .user-avatar-circle {
    display: none;
  }

  .mobile-search-toggle-btn {
    display: flex !important;
    width: 34px;
    height: 34px;
  }

  .icon-action-btn {
    width: 34px;
    height: 34px;
  }

  .header-nav-actions {
    gap: 6px;
    flex-shrink: 0;
  }

  /* General Mobile Sections */
  .mobile-section {
    padding: 32px 14px;
    width: 100%;
    box-sizing: border-box;
  }

  .mobile-section-header {
    text-align: center;
    margin-bottom: 20px;
  }

  .mobile-section-sub {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--color-gold-deep);
    text-transform: uppercase;
    display: block;
    margin-bottom: 5px;
  }

  .mobile-section-title {
    font-family: var(--font-serif);
    font-size: 22px;
    font-weight: 700;
    color: var(--color-maroon);
    line-height: 1.2;
  }

  /* Mobile Hero Section */
  .mobile-hero-container {
    background-color: var(--color-maroon);
    padding: 0 0 20px 0;
  }

  .mobile-hero-banner {
    position: relative;
    width: 100%;
    overflow: hidden;
  }

  .mobile-hero-banner img {
    width: 100%;
    height: auto;
    display: block;
  }

  .mobile-hero-content {
    padding: 18px 14px 4px;
  }

  .mobile-hero-title-box {
    text-align: center;
    margin-bottom: 16px;
    color: #FFFDF7;
  }

  .mobile-hero-sub {
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--color-gold-light);
    text-transform: uppercase;
  }

  .mobile-hero-h1 {
    font-family: var(--font-serif);
    font-size: 24px;
    font-weight: 700;
    line-height: 1.15;
    margin: 6px 0 14px;
    color: #FFFDF7;
  }

  .mobile-quick-actions {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
  }

  .mobile-action-pill {
    flex: 1;
    padding: 10px 6px;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    text-align: center;
    color: #FFFDF7;
    text-decoration: none !important;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
  }

  .mobile-action-pill:active {
    background: rgba(255, 255, 255, 0.22);
  }

  .mobile-product-card {
    background: #FAF8F5;
    border: 1px solid #EBE4DD;
    border-radius: 8px;
    padding: 16px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  }

  .mobile-product-tag {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.4px;
    color: var(--color-gold-deep);
    text-transform: uppercase;
    margin-bottom: 4px;
  }

  .mobile-product-title {
    font-family: var(--font-serif);
    font-size: 18px;
    font-weight: 700;
    color: var(--color-maroon);
    margin-bottom: 8px;
    line-height: 1.25;
  }

  .mobile-product-pricing {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
  }

  .mobile-product-btn {
    width: 100%;
    padding: 12px;
    background: var(--color-maroon);
    color: #FFFFFF;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-align: center;
    cursor: pointer;
    border: none;
    display: block;
    box-shadow: 0 4px 12px rgba(99, 0, 13, 0.3);
  }

  /* Mobile Concierge Suite */
  .mobile-concierge-suite {
    background: linear-gradient(180deg, #4A000A 0%, #63000D 100%);
    padding: 28px 14px;
  }

  .mobile-concierge-card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 12px;
    padding: 22px 16px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  }

  .concierge-crown {
    font-size: 28px;
    margin-bottom: 6px;
  }

  .mobile-concierge-btns-stack {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 18px;
  }

  /* Mobile Categories Grid */
  .mobile-categories-section {
    background-color: #FFF8F5;
  }

  .mobile-categories-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .mobile-cat-card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    display: block;
    transition: transform 0.2s ease;
    border: 1px solid #ECE4DF;
  }

  .mobile-cat-card img {
    width: 100%;
    height: auto;
    display: block;
  }

  .mobile-cat-card:active {
    transform: scale(0.98);
  }

  /* Mobile Bestsellers Grid */
  .mobile-bestsellers-section {
    background-color: #FAF2EE;
  }

  .mobile-bestsellers-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .mobile-best-card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    background: #FFFFFF;
    cursor: pointer;
    transition: transform 0.2s ease;
    border: 1px solid #EBE4DD;
  }

  .mobile-best-card img {
    width: 100%;
    height: auto;
    display: block;
  }

  .mobile-best-card:active {
    transform: scale(0.98);
  }

  /* Mobile Everyday Section */
  .mobile-everyday-section {
    background-color: #FFF8F5;
  }

  .mobile-everyday-card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    background: #FFFFFF;
    border: 1px solid #EBE4DD;
  }

  .mobile-everyday-card img {
    width: 100%;
    height: auto;
    display: block;
  }

  /* Mobile Story Section */
  .mobile-story-section {
    background-color: #EEE7E3;
  }

  .mobile-story-card {
    background: #FFFFFF;
    border-radius: 8px;
    padding: 18px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    border: 1px solid #E2D9D3;
  }

  /* Mobile Testimonials */
  .mobile-testimonials-section {
    background-color: #FFF8F5;
  }

  .mobile-testimonial-card {
    background: #FFFFFF;
    border-radius: 8px;
    padding: 18px;
    border: 1px solid #ECE4DE;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  }

  /* Mobile Instagram Lookbook */
  .mobile-insta-section {
    background-color: #FAF2EE;
  }

  .mobile-insta-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .mobile-insta-item {
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    border: 1px solid #EAE3DC;
  }

  .mobile-insta-item img {
    width: 100%;
    height: auto;
    display: block;
  }

  /* Mobile Footer */
  .footer-main {
    grid-template-columns: 1fr;
    gap: 28px;
    padding: 36px 16px 28px;
  }

  .footer-brand-col {
    padding-right: 0;
  }

  .footer-bottom-inner {
    flex-direction: column;
    text-align: center;
    gap: 12px;
  }

  .footer-bottom-links {
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
  }

  /* Modals on Mobile */
  .modal-dialog {
    max-width: 95% !important;
    margin: 10px auto;
  }

  .drawer-container {
    max-width: 85% !important;
  }
}

@media (max-width: 480px) {
  .drawer-container {
    max-width: 100% !important;
  }

  .vip-salon-form {
    flex-direction: column;
    gap: 8px;
  }

  .vip-salon-input {
    border-radius: 4px;
    width: 100%;
  }

  .vip-salon-btn {
    border-radius: 4px;
    width: 100%;
  }

  .mobile-quick-actions {
    flex-direction: column;
  }
}
'''

# Append or replace mobile styles in css/style.css
if '.mobile-only' in css:
    # replace from .mobile-only
    m_idx = css.find('/* Mobile Quick Elements */')
    if m_idx != -1:
        css = css[:m_idx] + mobile_css_additions
    else:
        css += '\n' + mobile_css_additions
else:
    css += '\n' + mobile_css_additions

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated css/style.css with responsive architecture!')
