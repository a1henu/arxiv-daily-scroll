---
layout: default
title: Beyond the Visible: Disocclusion-Aware Editing via Proxy Dynamic Graphs
---

# Beyond the Visible: Disocclusion-Aware Editing via Proxy Dynamic Graphs
**arXiv**：[2512.13392v1](https://arxiv.org/abs/2512.13392) · [PDF](https://arxiv.org/pdf/2512.13392.pdf)  
**作者**：Anran Qi, Changjian Li, Adrien Bousseau, Niloy J. Mitra  

**一句话要点**：提出代理动态图方法以解决图像转视频中用户控制新显露区域内容的问题

**关键词**：图像转视频生成, 代理动态图, 运动控制, 外观合成, 用户编辑, 去遮挡区域

## 3 点简述
- 核心问题：现有图像转视频方法难以生成可预测的关节运动并控制新显露区域内容
- 方法要点：使用轻量级代理动态图分离运动指定与外观合成，无需训练
- 实验或效果：在关节物体、家具等场景中优于现有方法，实现可控运动与外观编辑

## 摘要（原文）

> We address image-to-video generation with explicit user control over the final frame's disoccluded regions. Current image-to-video pipelines produce plausible motion but struggle to generate predictable, articulated motions while enforcing user-specified content in newly revealed areas. Our key idea is to separate motion specification from appearance synthesis: we introduce a lightweight, user-editable Proxy Dynamic Graph (PDG) that deterministically yet approximately drives part motion, while a frozen diffusion prior is used to synthesize plausible appearance that follows that motion. In our training-free pipeline, the user loosely annotates and reposes a PDG, from which we compute a dense motion flow to leverage diffusion as a motion-guided shader. We then let the user edit appearance in the disoccluded areas of the image, and exploit the visibility information encoded by the PDG to perform a latent-space composite that reconciles motion with user intent in these areas. This design yields controllable articulation and user control over disocclusions without fine-tuning. We demonstrate clear advantages against state-of-the-art alternatives towards images turned into short videos of articulated objects, furniture, vehicles, and deformables. Our method mixes generative control, in the form of loose pose and structure, with predictable controls, in the form of appearance specification in the final frame in the disoccluded regions, unlocking a new image-to-video workflow. Code will be released on acceptance. Project page: https://anranqi.github.io/beyondvisible.github.io/

