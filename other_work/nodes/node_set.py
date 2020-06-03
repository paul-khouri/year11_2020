def get_set():
    n_l_l = { "left": None,"right":None,"parent": None,
              "content": "Node Left Left"
        }
    n_l_r = {"left":None,"right":None,"parent": None,
        "content": "Node Left Right"
        }
    n_r_l= {"left":None,"right":None,"parent": None,
        "content": "Node Left Right Left"
        }
    n_r_r= {"left":None,"right":None,"parent": None,
        "content": "Node Right Right "
        }
    n_l = {"left":n_l_l,"right":n_l_r,"parent": None,
        "content": "Node Left "
        }
    n_r = {"left":n_r_l,"right":n_r_r,"parent": None,
        "content": "Node Right "
        }
    n = {"left":n_l,"right":n_r,"parent": None,
        "content": "Node "
        }
    n_r["parent"] = n
    n_l["parent"] = n
    n_l_l["parent"] = n_l
    n_l_r["parent"] = n_l
    n_r_l["parent"] = n_r
    n_r_r["parent"] = n_r
  
    return n
