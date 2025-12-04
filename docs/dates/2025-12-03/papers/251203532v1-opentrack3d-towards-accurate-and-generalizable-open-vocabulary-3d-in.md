---
layout: default
title: OpenTrack3D: Towards Accurate and Generalizable Open-Vocabulary 3D Instance Segmentation
---

# OpenTrack3D: Towards Accurate and Generalizable Open-Vocabulary 3D Instance Segmentation
**arXiv**：[2512.03532v1](https://arxiv.org/abs/2512.03532) · [PDF](https://arxiv.org/pdf/2512.03532.pdf)  
**作者**：Zhishan Zhou, Siyuan Wei, Zengran Wang, Chunjie Wang, Xiaosheng Yan, Xiao Liu  

**一句话要点**：提出OpenTrack3D框架，通过视觉-空间跟踪器和多模态大语言模型，实现无网格场景下的开放词汇3D实例分割。

**关键词**：开放词汇3D实例分割, 视觉-空间跟踪, 多模态大语言模型, 无网格处理, 跨视图一致性, 组合查询推理

## 3 点简述
- 现有方法依赖数据集特定提案或网格超点，难以泛化至无网格新场景；CLIP分类器对组合查询推理弱。
- 采用视觉-空间跟踪器在线构建跨视图一致提案，并可选超点细化；用多模态大语言模型替换CLIP增强组合推理。
- 在ScanNet200等基准上实现先进性能，展示强泛化能力，核心流程完全无网格。

## 摘要（原文）

> Generalizing open-vocabulary 3D instance segmentation (OV-3DIS) to diverse, unstructured, and mesh-free environments is crucial for robotics and AR/VR, yet remains a significant challenge. We attribute this to two key limitations of existing methods: (1) proposal generation relies on dataset-specific proposal networks or mesh-based superpoints, rendering them inapplicable in mesh-free scenarios and limiting generalization to novel scenes; and (2) the weak textual reasoning of CLIP-based classifiers, which struggle to recognize compositional and functional user queries. To address these issues, we introduce OpenTrack3D, a generalizable and accurate framework. Unlike methods that rely on pre-generated proposals, OpenTrack3D employs a novel visual-spatial tracker to construct cross-view consistent object proposals online. Given an RGB-D stream, our pipeline first leverages a 2D open-vocabulary segmenter to generate masks, which are lifted to 3D point clouds using depth. Mask-guided instance features are then extracted using DINO feature maps, and our tracker fuses visual and spatial cues to maintain instance consistency. The core pipeline is entirely mesh-free, yet we also provide an optional superpoints refinement module to further enhance performance when scene mesh is available. Finally, we replace CLIP with a multi-modal large language model (MLLM), significantly enhancing compositional reasoning for complex user queries. Extensive experiments on diverse benchmarks, including ScanNet200, Replica, ScanNet++, and SceneFun3D, demonstrate state-of-the-art performance and strong generalization capabilities.

