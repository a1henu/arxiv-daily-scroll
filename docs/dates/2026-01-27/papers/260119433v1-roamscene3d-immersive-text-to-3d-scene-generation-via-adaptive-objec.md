---
layout: default
title: RoamScene3D: Immersive Text-to-3D Scene Generation via Adaptive Object-aware Roaming
---

# RoamScene3D: Immersive Text-to-3D Scene Generation via Adaptive Object-aware Roaming
**arXiv**：[2601.19433v1](https://arxiv.org/abs/2601.19433) · [PDF](https://arxiv.org/pdf/2601.19433.pdf)  
**作者**：Jisheng Chu, Wenrui Li, Rui Zhao, Wangmeng Zuo, Shifeng Chen, Xiaopeng Fan  

**一句话要点**：提出RoamScene3D框架，通过自适应对象感知漫游实现沉浸式文本到3D场景生成。

**关键词**：文本到3D场景生成, 自适应漫游, 场景图推理, 运动注入修复, 沉浸式生成

## 3 点简述
- 现有方法存在空间盲区，依赖预定义轨迹，无法理解语义布局和推断遮挡内容。
- 利用视觉语言模型构建场景图，指导相机感知对象边界并规划自适应漫游轨迹。
- 引入运动注入修复模型，在合成全景数据集上微调，实验显示显著优于现有方法。

## 摘要（原文）

> Generating immersive 3D scenes from texts is a core task in computer vision, crucial for applications in virtual reality and game development. Despite the promise of leveraging 2D diffusion priors, existing methods suffer from spatial blindness and rely on predefined trajectories that fail to exploit the inner relationships among salient objects. Consequently, these approaches are unable to comprehend the semantic layout, preventing them from exploring the scene adaptively to infer occluded content. Moreover, current inpainting models operate in 2D image space, struggling to plausibly fill holes caused by camera motion. To address these limitations, we propose RoamScene3D, a novel framework that bridges the gap between semantic guidance and spatial generation. Our method reasons about the semantic relations among objects and produces consistent and photorealistic scenes. Specifically, we employ a vision-language model (VLM) to construct a scene graph that encodes object relations, guiding the camera to perceive salient object boundaries and plan an adaptive roaming trajectory. Furthermore, to mitigate the limitations of static 2D priors, we introduce a Motion-Injected Inpainting model that is fine-tuned on a synthetic panoramic dataset integrating authentic camera trajectories, making it adaptive to camera motion. Extensive experiments demonstrate that with semantic reasoning and geometric constraints, our method significantly outperforms state-of-the-art approaches in producing consistent and photorealistic scenes. Our code is available at https://github.com/JS-CHU/RoamScene3D.

