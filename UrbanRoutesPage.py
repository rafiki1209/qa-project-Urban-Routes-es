class UrbanRoutesPage:

    # se agregó clase y archivo UrbanRoutesPage de acuerdo a revision entrega 1

    def __init__(self,driver):
        self.driver = driver

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def set_from(self,address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def pide_taxi(self):
        self.driver.find_element(*self.pedir_taxi_btn).click()

    def set_tarifa(self):
        self.driver.find_element(*self.tarifa).click()

    def set_numero_tel(self):
        self.driver.find_element(*self.numero_tel).click()

    def set_phone(self, number_phone):
        self.driver.find_element(*self.phone_field).send_keys(number_phone)

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')
    
    def set_metodo_de_pago(self):
        self.driver.find_element(*self.metodo_de_pago).click()
        
    def set_efectivo(self):
        self.driver.find_element(*self.efectivo_btn).click()    
        
    def set_agregar_card_plus_btn(self):
        self.driver.find_element(*self.agregar_card_plus_btn).click()

    def set_agregar_btn(self):
        self.driver.find_element(*self.agregar_btn).click() 

    def set_card_number(self,number_card):
        self.driver.find_element(*self.card_numero).send_keys(number_card)
        
    def set_card_code_number(self,code_card_number):
        self.driver.find_element(*self.code_card_field).send_keys(code_card_number)     

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')
    
    def get_card(self):
        return self.driver.find_element(*self.card_number).get_property('value')
    
    def get_code(self):
        return self.driver.find_element(*self.code_card_number).get_property('value') 

    def set_siguiente_btn(self):
        self.driver.find_element(*self.siguiente_btn).click()

    def set_confirmar_btn(self):
        self.driver.find_element(*self.confirmar_btn).click()

    def set_cerrar_code_tel(self):
        self.driver.find_element(*self.cerrar_code_tel).click()
        
    def cerrar_metodo_de_pago(self):
        self.driver.find_element(*self.cerrar_metodo_de_pago).click()
        
    def set_mensaje_conductor(self,mensaje_cond):
        self.driver.find_element(*self.comment_driver).send_keys(mensaje_cond)
        
    def get_mensaje_conductor(self):
        return self.driver.find_element(*self.comment_driver)get_property('value')
    
    def set_manta_pañuelos(self):
        self.driver.find_element(self).send_keys(mensaje_cond)

    def set_helados_counter(self):
        self.driver.find_element(*self.comment_driver).send_keys(mensaje_cond)

    def set_reservar_btn(self):
        self.driver.find_element(*self.comment_driver).send_keys(mensaje_cond)
    
    
    # Metodos de Wait de acuerdo a la revisión de 1ra entrega
  
    def wait_for_load_field_from(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(from_field))
    def wait_for_load_button_pedir_taxi(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(pedir_taxi_btn))
    def wait_for_load_button_tarifa(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(tarifa))
    def wait_for_load_field_num_tel(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(phone_field))
    def wait_for_load_button_siguiente(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(siguiente_btn))
    def wait_for_load_phone_code(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(phone_code))
    def wait_for_load_button_confirmar(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(confirmar_btn))
    def wait_for_load_cerrar_tel_code(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located( cerrar_code_tel))
    def wait_for_load_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(metodo_de_pago))
    def wait_agregar_card_plus_btn(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(agregar_card_plus_btn))
    def wait_agregar_btn(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(agregar_btn))
    def wait_card_number(self,number_card):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(card_numero))        
    def wait_card_code_number(self,code_card_number):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(code_card_field))  
    def wait_for_load_cerrar_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(cerrar_metodo_de_pago))
    def wait_for_load_mensaje_conductor(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(comment_driver))
    def wait_for_load_sw_manta_pañuelos(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(sw-manta-pañuelos))
    def wait_for_load_helados_counter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(helados_counter))
    def wait_for_load_button_reservar(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(reservar_btn))
        
    
    
