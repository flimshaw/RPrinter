require 'spec_helper'

describe "entities/show" do
  before(:each) do
    @entity = assign(:entity, stub_model(Entity,
      :author => "Author",
      :tag => "Tag",
      :data => ""
    ))
  end

  it "renders attributes in <p>" do
    render
    # Run the generator again with the --webrat flag if you want to use webrat matchers
    rendered.should match(/Author/)
    # Run the generator again with the --webrat flag if you want to use webrat matchers
    rendered.should match(/Tag/)
    # Run the generator again with the --webrat flag if you want to use webrat matchers
    rendered.should match(//)
  end
end
