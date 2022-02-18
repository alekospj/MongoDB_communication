

# Dash & Plotly
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px

#Python
import os

#Others
import base64
import pandas as pd

#My tools
from toolbox import create_full_dir
from mongoTool import mongo_tool
from visualization import visuzlize


# #Read Users
# users_all = pd.read_csv(os.getcwd() + "\\assets\\accounts.csv")


UPLOAD_DIRECTORY = create_full_dir('data/uploaded/')




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

######################## Authenticasion here ####################
# pas = {}
# for i in range(0, len(users_all)):
#     case = {users_all['name'].loc[i]: users_all['password'].loc[i]}
#     pas.update(case)
#
# auth = dash_auth.BasicAuth(app, pas)

############## Here we are starting the body of the Dash app####################

app.layout = html.Div(
    className='body',
    children=[
    dbc.Row(className = 'header',
            children=[
                dbc.Col([html.H1(['MongoDB Show'])]),
                dbc.Col([]),
                ]
            ),

# Here I am starting my Tabs
dcc.Tabs([
    ##########################################   TAB 1 ################################################################
    dcc.Tab(className='Tabs', label='Mongo Collections', children=[

    ################  First Row ##########################################
    dbc.Row(className='rowNormal', children=[

        dbc.Col([
            html.P("Insert your Mongo Key:"),
            dcc.Textarea(
                id='textarea-mongokey',
                className='input-text',
                style={
                    "width": "80%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                }
            )

        ]),
        dbc.Col([
            dbc.Button(id = 'btn-enable-key',
                        className='button-gen',
                        n_clicks=0,
                        children='Enable Key'
                        ),
            html.Div(id = 'info-button-key'),

        ]),
        dbc.Col([]),
        dbc.Col([]),

        ]), # Ending of First Row
    ################  Second Row #########################################
    dbc.Row(className='row-barrier' ,children = [html.Br(id = '4233')]),

    ################  Third Row ##########################################

    dbc.Row([
        dbc.Col([
            html.P('The available databases:'),
            dcc.Dropdown(
                id='available-databases',
                className='dropdown-loc',
                clearable=True,
                placeholder='Select database',)
            ]),
        dbc.Col([
            html.P('The available Collections:'),
            dcc.Dropdown(
                id='available-collections',
                className='dropdown-loc',
                clearable=True,
                placeholder='Select Collection', )
        ]),
        dbc.Col([]),
        dbc.Col([]),

    ]), # End of Third Row

    ################  Third Row #########################################
    dbc.Row(className='row-barrier', children=[html.Br(id='4773')]),



    ################  Fourth Row ##########################################
    dbc.Row(className='rowNormal', children=[

        dcc.Graph(id='graph-collections', className='graph-results')

    ]),  # End of second Row

    ]),  # End of Tab 1


##########################################   TAB 2 ################################################################
dcc.Tab(className='Tabs', label='Upload Data', children=[

    ################  Fisth Row ##########################################
    dbc.Row(className='rowNormal',children=[
        dbc.Col(id = 'row1', children =[
            html.P("Upload new files:"),
            dcc.Upload(
                id = 'upload-data',
                className='Upload',
                children=[html.Div(['Drag and Drop or ',html.A('Select Files')])],
                style={
                    "width": "80%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                }
            ),
            html.Div(id='file-name', className='div-in')
        ]),
        dbc.Col([
            html.P("Select File for Collection:"),
            dcc.Dropdown(
                id='select-file',
                className='dropdowm',
                clearable=True,
                placeholder='Select File', )

        ]),
        dbc.Col([

        ]),
        dbc.Col([]),
    ]), # End of Row 1
    ################  Third Row #########################################
    dbc.Row(className='row-barrier', children=[html.Br(id='dfdf')]),


    ################  Fourth Row ##########################################
    dbc.Row(className='rowNormal', children=[
        dbc.Col([
            html.P('Set Database to add:'),
            dcc.Input(id="input-database",className='input-vals', type="text", placeholder="",
                      style={
                          "width": "80%",
                          "height": "40px",
                          "lineHeight": "60px",
                          "borderWidth": "1px",
                          "textAlign": "center",
                          "margin": "10px",
                          "borderRadius": "5px",
                      }),

            html.P('Set Collection to add:'),
            dcc.Input(id="input-collection", className='input-vals', type="text", placeholder="",
                      style={
                          "width": "80%",
                          "height": "40px",
                          "lineHeight": "60px",
                          "borderWidth": "1px",
                          "textAlign": "center",
                          "margin": "10px",
                          "borderRadius": "5px",
                      }),

            dbc.Button(id='btn-add-collection',
                       className='button-gen',
                       n_clicks=0,
                       children='Add',
                       style= {"textAlign": "center",
                                "margin": "10px"}
                       ),
            html.Div(id = 'res-upload'),

        ]),
        dbc.Col([

        ]),
        dbc.Col([

        ]),
        dbc.Col([]),
    ]),  # End of Third Row
]), # End of Tab 2

##########################################   TAB 2 ################################################################
dcc.Tab(className='Tabs', label='Delete Data', children=[

    dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.P('The available Databases:'),
                    dcc.Dropdown(
                        id='drop-db-del',
                        className='dropdown-loc',
                        clearable=True,
                        placeholder='Select Database'),
                ]),
            dbc.Row([
                html.P('The available Collections:'),
                dcc.Dropdown(
                    id='drop-coll-del',
                    className='dropdown-loc',
                    clearable=True,
                    placeholder='Select Collection'),
            ]),
            dbc.Row([
                dbc.Button(id='btn-dlt-collection',
                           className='button-del',
                           n_clicks=0,
                           children='Delete',
                           ),
                html.Div(id = 'div-res-del',className = 'results-div')

            ]),



        ]), # End of Column 1

        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
    ]),



]), # End of tab 3


]) # End of Tabs


]) # End of Layout here

##############################################################################################################
###########################    Starting of Callbacks    ######################################################
##############################################################################################################

##############################################################################################################
###########################   DELETE Collection DB          ##################################################
##############################################################################################################
@app.callback(
    Output( 'div-res-del','children'),
    [Input('drop-db-del', 'value'),
     Input('drop-coll-del', 'value'),
     Input('textarea-mongokey', 'value'),
     Input('btn-dlt-collection','n_clicks')],
)
def delete_data(del_datbase,del_collection,key_mongo,n_clicks):
    if del_datbase == None and del_collection == None:
        raise PreventUpdate

    elif del_datbase != None and del_collection != None:
        if n_clicks ==0:
            return 'Press Delete button'
        elif n_clicks !=0:
            # Creating the object to communicate with the Mongo DB
            data_arch = mongo_tool(key_mongo)

            data_arch.drop_collection(del_datbase,del_collection)

            return del_collection +' from '+del_datbase+' deleted!'


##############################################################################################################
###########################    UPDATE Collections for DELETE     #############################################
##############################################################################################################
@app.callback(
    Output('drop-coll-del', 'options'),
    [Input('drop-db-del', 'value'),
     Input('textarea-mongokey', 'value')],
)
def update_for_delete_collections(del_datbase,key_mongo):

    # Creating the object to communicate with the Mongo DB
    data_arch = mongo_tool(key_mongo)

    collections = data_arch.show_collections(del_datbase)

    opts  =[{'label': x, 'value': x} for x in collections]

    return opts


##############################################################################################################
###########################    UPDATE Dabases for DELETE     #################################################
##############################################################################################################
@app.callback(
    Output('drop-db-del', 'options'),
    [Input('textarea-mongokey', 'value')],
)
def update_for_delete_databases(key_mongo):
    # Creating the object to communicate with the Mongo DB
    data_arch = mongo_tool(key_mongo)

    dataBases   = data_arch.show_databases()

    opts1  =[{'label': x, 'value': x} for x in dataBases]

    return opts1


##############################################################################################################
###########################    UPDATE AVAILABLE COLLECTIONS      #############################################
##############################################################################################################
@app.callback(
    Output('res-upload', 'children'),
    [Input('input-database', 'value'),
     Input('input-collection', 'value'),
     Input('btn-add-collection','n_clicks'),
     Input('select-file','value'),
     Input('textarea-mongokey','value')
     ],
)
def update_collection(in_database,in_collection,btn_clicks,sel_file,key_mongo):

    if in_database == None or in_collection == None:
        raise PreventUpdate

    elif in_database !=None and in_collection !=None and btn_clicks ==0:

        return 'Press button to add in MongoDb'

    elif in_database !=None and in_collection !=None and btn_clicks !=0:

        # Reading the selected file
        df = pd.read_csv(UPLOAD_DIRECTORY + sel_file)

        # Creating the object to communicate with the Mongo DB
        data_arch = mongo_tool(key_mongo)

        # Uploading the csv file into Mongo as collection
        data_arch.upload_df(df,in_database,in_collection)

        # Removing the file from the application folder
        os.remove(UPLOAD_DIRECTORY + sel_file)


        return 'The collection '+in_collection +' added to '+in_database




##############################################################################################################
###########################    UPDATE AVAILABLE COLLECTIONS      #############################################
##############################################################################################################
@app.callback(
    Output('available-collections', 'options'),
    [Input('available-databases', 'value'),
     Input('textarea-mongokey', 'value')],
)
def available_collections_update(db_name,key_mongo):

    if db_name == None:
        raise PreventUpdate
    else:

        data_arch = mongo_tool(key_mongo)

        collections = data_arch.show_collections(db_name)

        opts =[{'label': x, 'value': x} for x in collections]

        return opts



##############################################################################################################
###########################     ENABLE MONGO KEY        ######################################################
##############################################################################################################
@app.callback(
    Output('info-button-key', 'children'),
    Output('available-databases', 'options'),
    [Input('btn-enable-key', 'n_clicks'),
     Input('textarea-mongokey','value')],
)
def enable_key(n_clicks,key_mongo):

    if n_clicks == 0:
        opts = [{'label': x, 'value': x} for x in []]

        return 'press to enable',opts

    elif n_clicks !=0 and key_mongo == None:
        opts = [{'label': x, 'value': x} for x in ['Q','Z']]

        return 'copy paste your Mongo key',opts

    elif n_clicks !=0 and key_mongo !=None:

        data_arch = mongo_tool(key_mongo)

        opts = [{'label': x, 'value': x} for x in data_arch.show_databases()]

        return 'Mongo Enabled',opts



##############################################################################################################
###########################     UPDDATE GRAPH RESULTS   ######################################################
##############################################################################################################
# Functionality for upload file
@app.callback(
    Output('graph-collections', 'figure'),
    [Input('textarea-mongokey','value'),
     Input('available-databases','value'),
    Input('available-collections','value')],
)
def graph_results(mongoKey,db_sel,col_sel):

    if db_sel == None or col_sel == None:
        raise PreventUpdate
    else:

        # Here I am pulling the data from the selected collection from Mongo DB to make the graph
        data_arch = mongo_tool(mongoKey)
        df = data_arch.retrieve_collection_df(db_sel,col_sel)

        fig = visuzlize(df)

        return fig


##############################################################################################################
###########################     UPLOAD FILE  #################################################################
##############################################################################################################

# Functionality for upload file
@app.callback(
    Output('file-name', 'children'),
    Output('select-file', 'options'),
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')],
)
def upload_pdf_to_server(content, filename):

    if not content:

        opt = [{'label': x, 'value': x} for x in os.listdir(UPLOAD_DIRECTORY)]

        return 'No files',opt


    data = content.encode("utf8").split(b";base64,")[1]

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(base64.decodebytes(data))

    opt = [{'label': x, 'value': x} for x in os.listdir(UPLOAD_DIRECTORY)]

    # Extracting Information
    return filename +' uploaded!',opt




if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=9666, debug=False, use_reloader=False)
