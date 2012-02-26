require 'spec_helper'

describe "entities/index" do
  before(:each) do
    assign(:entities, [
      stub_model(Entity,
        :author => "Author",
        :tag => "Tag",
        :data => ""
      ),
      stub_model(Entity,
        :author => "Author",
        :tag => "Tag",
        :data => ""
      )
    ])
  end

  it "renders a list of entities" do
    render
    # Run the generator again with the --webrat flag if you want to use webrat matchers
    assert_select "tr>td", :text => "Author".to_s, :count => 2
    # Run the generator again with the --webrat flag if you want to use webrat matchers
    assert_select "tr>td", :text => "Tag".to_s, :count => 2
    # Run the generator again with the --webrat flag if you want to use webrat matchers
    assert_select "tr>td", :text => "".to_s, :count => 2
  end
end
