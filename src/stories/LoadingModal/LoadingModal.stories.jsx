import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import LoadingModal from "./LoadingModal"





// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Modal de carga',
  component: LoadingModal,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Modal_de_carga = (args) => {
return <LoadingModal />;
}