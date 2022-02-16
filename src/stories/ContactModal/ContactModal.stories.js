import React from 'react';
import ContactModal from './ContactModal';
import { CustomDocumentationComponent } from './documentacion2';



// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Contacto',
  component: ContactModal,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const  Modal_de_contacto = (args) => {
return <ContactModal />;
}