pcf_storyscapes
========================

Installation
------------

Install the PWS CLI (https://docs.run.pivotal.io/starting/), configure your credentials then::

   $ git clone https://github.com/MapStory/pcf_storyscapes.git
   $ cd pcf_storyscapes
Initial push
   $ cf push -c "bash ./init_db.sh"
Additional pushes
   $ cf push
