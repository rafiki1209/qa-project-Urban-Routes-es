class UrbanRoutesWait:
    def __init__(self, driver):
        self.driver = driver
        
        # Metodos de Wait de acuerdo a la revisión de 1ra entrega
  
    # Prueba1 Route
    def wait_for_load_field_from(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.from_field))
    # Prueba2 Tarifa
    def wait_for_load_button_pedir_taxi(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.pedir_taxi_btn))
    def wait_for_load_button_tarifa(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.tarifa))
    # Prueba3 Phone
    def wait_for_load_phone_btn(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.numero_tel))
    def wait_for_load_field_num_tel(self):
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.phone_field))
    def wait_for_load_button_siguiente(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.siguiente_btn))
    def wait_for_load_phone_code(self):        
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.phone_code))
    def wait_for_load_button_confirmar(self):        
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.confirmar_btn))
    def wait_for_load_cerrar_tel_code(self):         
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.cerrar_code_tel))
    # Prueba4 Agregar Card
    def wait_for_load_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.metodo_de_pago))
    def wait_agregar_card_plus_btn(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.agregar_card_plus_btn))
    def wait_agregar_btn(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.agregar_btn))
    def wait_card_number(self,number_card):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.card_numero))    
    def wait_card_code_number(self,code_card_number):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.code_card_field))  
    def wait_for_load_cerrar_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.cerrar_metodo_de_pago_btn))
    # Prueba5 Mensaje al conductor
    def wait_for_load_mensaje_conductor(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.comment_driver))
    # Prueba6 Requisitos  sw manta pañuelos
    def wait_for_load_sw_manta_pañuelos(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.sw-manta-pañuelos))
    # Prueba7 contador Helados
    def wait_for_load_helados_counter(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.helados_counter))
    # Prueba8 Reservar
    def wait_for_load_button_reservar(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.reservar_btn))



