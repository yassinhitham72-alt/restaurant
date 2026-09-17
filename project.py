# 1. Importing extensions
import streamlit as st
import google.generativeai as ai 

# Adding AI assistant part
with st.sidebar: 
    st.header('Chat with our AI Assistant✨')
    key=st.secrets['API']

    
    # Gemini setup
    ai.configure(api_key=key)
    model = ai.GenerativeModel('gemini-3.5-flash')
    
    question = st.chat_input('Ask anything!')
    
    if question:
        # 1. User chat messge
        with st.chat_message('user'):
            st.write(question)
        
        # 2. AI chat message
        with st.chat_message('ai'):
            with st.spinner('Generating..✨'):
                prompt = f'''
                You are PizzaHub's AI Assistant.

                Answer the customer's question only if it is related to PizzaHub,
                its menu, prices, food, drinks, restaurant services, working hours,
                or ordering.
  
                If the question is not related to PizzaHub, politely say that you
                can only answer questions related to PizzaHub.

                Here is PizzaHub's complete menu:

                PIZZAS:
                - Margherita Pizza:
                    Small: 140 EGP
                    Medium: 180 EGP
                    Large: 200 EGP

                - Chicken Ranch:
                    Small: 170 EGP
                    Medium: 200 EGP
                    Large: 230 EGP

                - Pepperoni Pizza:
                    Small: 180 EGP
                    Medium: 220 EGP
                    Large: 250 EGP

                PASTA:
                - Fettuccine Alfredo: 180 EGP
                - Spaghetti Bolognese: 200 EGP
                - Pesto Penne: 190 EGP

                DRINKS:
                - Cola: 50 EGP
                - Sprite: 50 EGP
                - Orange Juice: 70 EGP
                - Water: 20 EGP

                RESTAURANT INFORMATION:
                - Working hours: 11 AM to 10 PM

                Important instructions:
                - Answer only PizzaHub-related questions.
                - Use only the information provided above when answering menu,
                  prices, and working-hours questions.
                - Do not invent menu items, prices, offers, ingredients, or services.
                - If the requested information is not provided above, say that you
                  do not have that information.
                - Keep answers clear, friendly, and concise.

                Customer question:
                {question}
                '''
                
                answer = model.generate_content(prompt)
                
                
            st.write(answer.text)
            
        
    

# 2. App title & caption
st.title(':shimmer[:red[Welcome to PizzaHub]]🍕', 
    text_alignment='center') 
st.subheader('The best Italian restuarant serving pizza & pasta!')

# 3. Creating app tabs
pizza_tab, pasta_tab, drinks_tab = st.tabs(
    ['Pizzas🍕', 'Pasta🍝', 'Drinks🍹'])

# 4. Building pizza tab
with pizza_tab:
    col1, col2, col3 = st.columns(3)
    sizes = ['Small', 'Medium', 'Large']
    
    with col1:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/product_50_1768290827.jpg')
        st.subheader('Magerita Pizza', text_alignment='center')
        
        # Adding the size option
        margerita_size = st.segmented_control('Size:', 
            options=sizes, key=1, default='Medium')
        
        # Margerita prices
        margerita_prices = {
            'Small':140,
            'Medium':180,
            'Large':200
        }
        # Displaying the price
        margertia_price = margerita_prices[margerita_size]
        st.write(f'Price: :red[**{margertia_price}**] EGP')
        
        # Selecting the quantity
        margerita_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='mrg_qty')
        
    with col2:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/Chicken-Ranch---Spicy-Korean.jpg')
        st.subheader('Chicken Ranch', text_alignment='center')
        
        # Adding the size option
        ranch_size = st.segmented_control('Size:', 
                    options=sizes, key=2, default='Medium')
        
        # Ranch prices
        ranch_prices = {
            'Small':170,
            'Medium':200,
            'Large':230
        }
        # Displaying the price
        ranch_price = ranch_prices[ranch_size]
        st.write(f'Price: :red[**{ranch_price}**] EGP')
        
        # Selecting the quantity
        ranch_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='rch_qty')
    
    with col3:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/product_9_1768291533.jpg')
        st.subheader('Pepperoni Pizza', text_alignment='center')
        
        # Adding the size option
        pepperoni_size = st.segmented_control('Size:', 
                    options=sizes, key=3, default='Medium')
        
        # Pepperoni prices
        pepperoni_prices = {
            'Small':180,
            'Medium':220,
            'Large':250
        }
        # Displaying the price
        pepperoni_price = pepperoni_prices[pepperoni_size]
        st.write(f'Price: :red[**{pepperoni_price}**] EGP')
        
        # Selecting the quantity
        pepperoni_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='ppr_qty')
        
# 7. Building pasta tab
with pasta_tab:
    col1, col2, col3 = st.columns(3)

    with col1:
        # Adding pasta image and name
        st.image(
            "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=600&h=450&fit=crop"
        )
        st.subheader('Fettuccine Alfredo', text_alignment='center', anchor=False)

        # Alfredo price
        alfredo_price = 180
        st.write(f'Price: :red[**{alfredo_price}**] EGP')

        # Selecting the quantity
        alfredo_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='alfredo_qty'
        )

    with col2:
        # Adding pasta image and name
        st.image(
            "https://images.unsplash.com/photo-1626844131082-256783844137?w=600&h=450&fit=crop"
        )
        st.subheader('Spaghetti', text_alignment='center')

        # Bolognese price
        bolognese_price = 200
        st.write(f'Price: :red[**{bolognese_price}**] EGP')

        # Selecting the quantity
        bolognese_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='bolognese_qty'
        )

    with col3:
        # Adding pasta image and name
        st.image(
            "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600&h=450&fit=crop"
        )
        st.subheader('Pesto Penne', text_alignment='center')

        # Pesto price
        pesto_price = 190
        st.write(f'Price: :red[**{pesto_price}**] EGP')

        # Selecting the quantity
        pesto_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='pesto_qty'
        )


# 8. Building drinks tab
with drinks_tab:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&h=450&fit=crop"
        )
        st.subheader('Cola', text_alignment='center')

        # Cola price
        cola_price = 50
        st.write(f'Price: :red[**{cola_price}**] EGP')

        # Selecting the quantity
        cola_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='cola_qty'
        )

    with col2:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1680404005217-a441afdefe83?w=600&h=450&fit=crop"
        )
        st.subheader('Sprite', text_alignment='center')

        # Sprite price
        sprite_price = 50
        st.write(f'Price: :red[**{sprite_price}**] EGP')

        # Selecting the quantity
        sprite_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='sprite_qty'
        )

    with col3:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=600&h=450&fit=crop"
        )
        st.subheader('Orange Juice', text_alignment='center', anchor=False)

        # Orange juice price
        orange_juice_price = 70
        st.write(f'Price: :red[**{orange_juice_price}**] EGP')

        # Selecting the quantity
        orange_juice_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='orange_juice_qty'
        )

    with col4:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1550505095-81378a674395?w=600&h=450&fit=crop"
        )
        st.subheader('Water', text_alignment='center')

        # Water price
        water_price = 20
        st.write(f'Price: :red[**{water_price}**] EGP')

        # Selecting the quantity
        water_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='water_qty'
        )

# Calculating total step 
total_price = (
    (margertia_price * margerita_qty) +
    (pepperoni_price * pepperoni_qty) +  
    (ranch_price * ranch_qty) +
    (alfredo_price * alfredo_qty) +
    (bolognese_price * bolognese_qty) +
    (pesto_price * pesto_qty) +
    (cola_price * cola_qty) +
    (sprite_price * sprite_qty) +
    (orange_juice_price * orange_juice_qty) +
    (water_price * water_qty)
)
st.divider()
if st.button('Calculate Total 💰', use_container_width=True, type='primary'):
    st.subheader(f'Total = {total_price} EGP')
