def configure_logging():
    current_date = time.strftime("%d-%m-%Y", time.localtime())
    log_file = createfile_nocollision(f"log_{current_date}", ".log")
        
    logging.basicConfig(filename=log_file, 
                        filemode="a", 
                        encoding='utf-8',
                        format="'%(asctime)s' - %(name)s → %(levelname)s: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)  
  
    with open(log_file, "w") as file_log:
        file_log.write(log_banner())
