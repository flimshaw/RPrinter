require 'spec_helper'

describe "entities/new" do
  before(:each) do
    assign(:entity, stub_model(Entity,
      :author => "",
      :type => "",
      :data => ""
    ).as_new_record)
  end

  it "renders new entity form" do
    render

    # Run the generator again with the --webrat flag if you want to use webrat matchers
    assert_select "form", :action => entities_path, :method => "post" do
      assert_select "input#entity_author", :name => "entity[author]"
      assert_select "input#entity_type", :name => "entity[type]"
      assert_select "input#entity_data", :name => "entity[data]"
    end
  end
end
