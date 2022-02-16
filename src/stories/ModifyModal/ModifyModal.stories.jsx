import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import ModifyModal from './ModifyModal';






// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Modal modificar usuarios',
  component: ModifyModal,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Modal_modificar_usuarios = (args) => {
return <ModifyModal />;
}