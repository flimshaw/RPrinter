require "net/http"
require "uri"
class EntitiesController < ApplicationController

    
  # GET /entities
  # GET /entities.xml
  def index
    @entities = Entity.all

    respond_to do |format|
      format.html # index.html.erb
      format.xml  { render :xml => @entities }
    end
  end

  # GET /entities/1
  # GET /entities/1.xml
  def show
    @entity = Entity.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.xml  { render :xml => @entity }
    end
  end

  def gather
    	# gather all new data from sources
      # todo - ADAPTER PATTERN!!!!
      
    	# todo - 
    	# SOURCE: dropbox  	  	
    	# SOURCE: docs.google.com?
    	# SOURCE: flimshaw.net irc?
    	# SOURCE: and many others!


    # SOURCE: twitter - http://search.twitter.com/search.json?q=from%3Aflimshaw OR from%3Aashleyluvspizza
  	#file_handle = open("http://search.twitter.com/search.json?q=from%3Aflimshaw OR from%3Aashleyluvspizza")
  	#document = Nokogiri::XML(file_handle)
  	#document/"xpath/search"

  	  url = "http://search.twitter.com/search.json?q=from%3Aflimshaw%20OR%20from%3Aashleyluvspizza"
      resp = Net::HTTP.get_response(URI.parse(url))
      data = resp.body
      # convert ot hash
      parsed_json = ActiveSupport::JSON.decode(data)
      logger.info(parsed_json)

      #parsed_json["results"].each do |longUrl, convertedUrl|
  	#  entity = Entity.new
  	#  assign json shit into entity
  	#  entity.save!
  end
  
  
  # GET /entities/new
  # GET /entities/new.xml
  def new
    @entity = Entity.new
   
    respond_to do |format|
      format.html # new.html.erb
      format.xml  { render :xml => @entity }
    end

  end

  # GET /entities/1/edit
  def edit
    @entity = Entity.find(params[:id])
  end

  # POST /entities
  # POST /entities.xml
  def create
    @entity = Entity.new(params[:entity])

    respond_to do |format|
      if @entity.save
        format.html { redirect_to(@entity, :notice => 'Entity was successfully created.') }
        format.xml  { render :xml => @entity, :status => :created, :location => @entity }
      else
        format.html { render :action => "new" }
        format.xml  { render :xml => @entity.errors, :status => :unprocessable_entity }
      end
    end
  end

  # PUT /entities/1
  # PUT /entities/1.xml
  def update
    @entity = Entity.find(params[:id])

    respond_to do |format|
      if @entity.update_attributes(params[:entity])
        format.html { redirect_to(@entity, :notice => 'Entity was successfully updated.') }
        format.xml  { head :ok }
      else
        format.html { render :action => "edit" }
        format.xml  { render :xml => @entity.errors, :status => :unprocessable_entity }
      end
    end
  end

  # DELETE /entities/1
  # DELETE /entities/1.xml
  def destroy
    @entity = Entity.find(params[:id])
    @entity.destroy

    respond_to do |format|
      format.html { redirect_to(entities_url) }
      format.xml  { head :ok }
    end
  end
end
