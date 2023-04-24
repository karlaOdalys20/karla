class Article:

  def __init__(self, title: str, abstract: str) -> None:
    self.title = title
    self.abstract = abstract


class BibFile:

  def __init__(self, file_name: str) -> None:
    self.articles: list[Article] = []
    archivo = open(file_name, 'r', encoding='utf-8')
    tmp_article = {'title': '', 'abstract': ''}
    for linea in archivo:
      linea = linea.strip()
      if (linea.startswith('@')):
        if (tmp_article['title'] == '' or tmp_article['abstract'] == ''):
          tmp_article = {'title': '', 'abstract': ''}
        elif (tmp_article['title'] != '' and tmp_article['abstract'] != ''):
          self.articles.append(
            Article(tmp_article['title'], tmp_article['abstract']))
          tmp_article = {'title': '', 'abstract': ''}
      elif (linea.startswith('title')):
        tmp_title = linea[7:-3]
        tmp_article['title'] = tmp_title
      elif (linea.startswith('abstract')):
        tmp_abstract = linea[10:-3]
        tmp_article['abstract'] = tmp_abstract
    archivo.close()
    self.articles.append(Article(tmp_article['title'],
                                 tmp_article['abstract']))


dicc_categorias = {
  "Geomorphology": [
    "landforms", "geomorphology", "topography", "hillslopes", "valley",
    "landscape", "dendritic", "basin", "meanders", "terrace", "floodplain",
    "fluvial geomorphology", "bedforms", "channel planform", "alluvial fans",
    "levees", "crevasse channel", "point bars", "cutbank",
    "alluvial environment", "fluvial environment", "alluvial delta"
  ],
  "Tectonism": [
    "lithosphere", "geodynamics", "tectonic plates", "uplift", "subsidence",
    "active margin", "passive margin", "subduction", "active faults",
    "strike-slip fault", "normal fault", "inverse fault", "focal mechanism"
  ],
  "Seismic Hazard": [
    "earthquake hazard", "seismic", "earthquake", "seismic wave", "P waves",
    "S waves", "landslide trigger", "tsunamis origin",
    "Mercalli intensity scale", "Richter magnitude scale", "soil liquefaction",
    "microseismic monitoring", "seismic risk", "seismic engineering"
  ],
  "Meteorology": [
    "weather regimes", "hydrometeorology", "extreme precipitation", "rainfall",
    "daily precipitation", "annual precipitation", "temperature rise",
    "maximum air temperature", "minimum air temperature", "extreme analysis"
  ],
  "Climatology": [
    "tropical climate", "ocean-atmosphere circulation", "climate change",
    "El Nino", "ENSO", "atmosphere", "ocean current"
  ],
  "Hydrological variables": [
    "extreme precipitation", "rainfall", "daily precipitation",
    "annual precipitation", "temperature rise", "maximum temperature",
    "minimum temperature", "extreme temperature", "evaporation",
    "evapotranspiration", "relative humidity", "solar radiation",
    "wind velocity", "wind direction"
  ],
  "Remote Sensing & GIS": [
    "remotely sensed", "imagery", "Earthdata", "orbits", "sensor", "GPM",
    "spatial resolution", "GIS", "Sentinel", "Landsat", "Spot",
    "Supervised Classification", "Remote Sensing Index",
    "RGB band combinations"
  ],
  "Water balance": [
    "hydrological cycle", "rainfall runoff modelling", "water balance",
    "hydrological modelling", "soil erosion", "basin", "watershed",
    "catchment", "rainfall", "runoff", "HRU", "landuse", "land use",
    "soil type", "soil horizon", "clay", "sand", "silt"
  ],
  "Ecohydrology": [
    "hydrobiology", "ecosystem", "ecosytem properties", "ecosystem functions",
    "abiotic-biotic interactions", "water-biota relations",
    "biogeochemical processes", "environmental flows", "habitat modelling"
  ],
  "Groundwater": [
    "groundwater", "aquifer", "aquitard", "soil conductivity", "piezometer",
    "groundwater pollution", "aquifer contamination", "hydraulic conductivity",
    "permeability", "rock formation", "water wells", "GRACE satellite",
    "groundwate geophysics", "hydrogeology"
  ],
  "Hydrodynamics": [
    "hydrodynamics", "river", "river routing", "river banks",
    "hydrodynamic modelling", "water diversion", "weir", "intake", "dike",
    "levees", "dam break", "flood", "flood risk", "flood risk management",
    "floodplain", "flood maps", "rating curve", "roughness", "Nash-Sutcliffe",
    "bathymetry"
  ],
  "Eco-hydraulics": [
    "nature based solutions", "blue green solutions",
    "climage change adaptation", "resillience", "environmental flows",
    "restoration", "fish passage", "wetland"
  ],
  "Morphodynamics": [
    "sediment production", "coastal erosion", "scour", "sediment transport",
    "bedload", "suspended sediments", "washload", "sedimentation"
  ],
  "Physical parameters": [
    "water temperature", "salinity", "total dissolved solids",
    "total sediment matter", "conductivity", "turbidity", "concentration",
    "plume", "color", "secchi depth"
  ],
  "Chemical parameters": [
    "inorganic nitrogen", "nitrites", "nitrates", "ammonium", "ammonia",
    "phosphorus", "phosphate", "silicate", "organic nitrogen",
    "organic phosphorus", "dissolved oxygen", "biochemical oxygen demand",
    "chemical oxygen demand", "chloride", "sulfate", "ammonia", "hardness",
    "potential hydrogen"
  ],
  "Organic matter": [
    "organic matter", "organic carbon in sediments",
    "organic carbon sinks and processes",
    "organic carbon in terrestrial environments",
    "organic carbon in water environments"
  ],
  "Eutrophication": [
    "high nutrient levels", "primary production", "phytoplankton",
    "blue-green algae", "algae bloom", "algal bloom"
  ],
  "Heavy metals":
  ["Arsenic", "Mercury", "Cadmiun", "Lead", "Nickel", "Chromium", "Antimony"],
  "Pesticides": ["pesticides", "fungicides", "plaguicides", "fumigation"],
  "Aquatic Ecotoxicology": ["toxic chemicals", "bio-accumulation"],
  "Freshwater Microbiology": [
    "bacterioplankton", "total coliforms", "fecal coliforms",
    "Escherichia Coli", "salmonella", "pseudomonas aeuroginosa", "bacteria"
  ],
  "Fauna Freshwater communities": [
    "phytoplankton", "zooplankton", "ichtyoplankton", "macroinvertebrates",
    "fish"
  ],
  "Fauna Terrestrial communities": [
    "invertebrates", "annelids", "arthropods-Insecta", "mollusca",
    "amphibians", "reptiles", "birds", "mammals"
  ],
  "Fauna-Flora Biogeography, genetics, and evolution": [
    "species geographic distribution", "phylogeography",
    "populations genetics", "phylogenetics"
  ],
  "Fauna-Flora Species Morphology":
  ["length-weight relations", "morphology changes", "evolution"],
  "Fauna-Flora Species conservation": [
    "conservation actions", "endemic species", "endangered species",
    "habitat restoration", "reforestation", "environmental education",
    "invasive species", "regulation of fishing and hunting activities",
    "climate change adapation", "habitat modelling"
  ],
  "Flora Freshwater communities": [
    "floating and submerged macrophytes", "invasive species",
    "response to eutrophication"
  ],
  "Flora Terrestrial communities": [
    "endemic species", "endangered species",
    "threatened species due to deforestation", "role"
  ],
  "Land use and water management": [
    "land use changes", "land use dynamics", "land cover",
    "land use management", "water management", "surface water", "groundwater",
    "water provision", "water supply", "water demand", "green water",
    "water availability", "wetland", "river basin", "catchment", "sub basin"
  ],
  "Erosion": [
    "sediment production", "nutrient flow", "basin erosion", "erosion",
    "soil erosion", "soil formation", "geomorphology", "runoff"
  ],
  "Rural socioeconomics": [
    "credit access", "farmer social capital", "farmer associations",
    "peasant agriculture", "family agriculture", "multi functional farming",
    "farmer assets", "agricultural productive unit", "traditional farming",
    "small scale farming", "peasant social capital", "peasant associations"
  ]
}

matriz = []
lista_columna_categoria = list(dicc_categorias.keys())
lista_fila_titulo = []


def crearMatriz(articulos):
  numero_fila = len(articulos.articles)
  numero_columna = len(dicc_categorias.keys())
  for i_fila in range(numero_fila):
    lista = []
    for i_columna in range(numero_columna):
      lista.append(0)
    matriz.append(lista)


def obtenerInfo(articulos):
  crearMatriz(articulos)
  i_articulo = 0
  for articulo in articulos.articles:
    lista_fila_titulo.append(articulo.title)
    llenarMatriz(articulo, i_articulo)
    i_articulo += 1
  return (matriz, lista_fila_titulo, lista_columna_categoria)
  # print("Matriz: ", matriz)
  # print("Filas: ", lista_fila_titulo)
  # print("Columnas: ", lista_columna_categoria)
  # print("Columnas len: ", len(lista_columna_categoria))


def llenarMatriz(articulo, i_articulo):
  i_categoria = 0
  for categoria in dicc_categorias:
    keywords = dicc_categorias[categoria]
    for keyword in keywords:
      if keyword.lower() not in articulo.title.lower():
        continue
      if not matriz[i_articulo][i_categoria] == 1:
        matriz[i_articulo][i_categoria] = 1
        break
    i_categoria += 1

  i_categoria = 0
  for categoria in dicc_categorias:
    keywords = dicc_categorias[categoria]
    for keyword in keywords:
      if keyword.lower() not in articulo.abstract.lower():
        continue
      if not matriz[i_articulo][i_categoria] == 1:
        matriz[i_articulo][i_categoria] = 1
        break
    i_categoria += 1


i_archivo = 1
lista_archivos = ['atrato01.bib','chira01.bib', 'colca01.bib']
for archivo in lista_archivos:
  bib = BibFile(archivo)
  print(f"Archivo{i_archivo} ", obtenerInfo(bib))
  i_archivo += 1
