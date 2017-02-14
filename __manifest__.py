# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.


{
    'name': "Theme Dusty",
    'description': 'Theme Dusty By 73Lines',
    'category': "Theme/Ecommerce",
    'version': "10.0.0.1",
    'author': "73Lines",

    'data': [
            'views/assets.xml',
            'views/mid_header.xml',
            'views/product_template.xml',
            'views/s_product_detail.xml',
            'views/customize_model.xml',

            # Snippets

            'views/snippet_custom_banner.xml',
            'views/snippet_parallex.xml',
            'views/snippet_three_images.xml',
            'views/snippet_footer.xml',

    ],
    'demo': [
        'data/nav_demo.xml',
        'data/brand_demo.xml',
        'data/s_footer_template.xml',
        'data/home_page.xml',

    ],


    'depends': [

        # Default Modules

        'website',
        'website_animate',

        # 73lines Depend Modules

        # Don't forget to see README file in order to how to install
        # In order to install complete theme, uncomment the following dependency.
        # Dependent modules are supplied in a zip file along with the theme,
        # if you have not received it,please contact us at
        # enquiry@73lines.com with proof of your purchase.

        # 'carousel_slider_73lines',
        # 'snippet_blog_carousel_73lines',
        # 'snippet_product_brand_carousel_73lines',
        # 'snippet_product_carousel_73lines',
        # 'snippet_product_category_carousel_73lines',
        # 'website_customize_model_73lines',
        # 'website_header_layout_73lines',
        # 'website_language_flag_73lines',
        # 'website_mega_menu_73lines',
        # 'website_product_categ_menu_and_banner_73lines',
        # 'website_product_comparison_73lines',
        # 'website_product_misc_options_73lines',
        # 'website_product_page_layout_73lines',
        # 'website_product_quick_view_73lines',
        # 'website_product_ribbon_73lines',
        # 'website_product_share_options_73lines',
        # 'website_user_wishlist_73lines',


    ],

    'images': [
        'static/description/dusty-banner.png',
    ],

    'price': 200,
     'license': 'Other proprietary',
    'currency': 'EUR',
    'live_test_url': 'http://theme-dusty.73lines.com/',
}
