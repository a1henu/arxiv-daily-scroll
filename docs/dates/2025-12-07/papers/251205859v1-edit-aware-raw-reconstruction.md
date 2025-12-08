---
layout: default
title: Edit-aware RAW Reconstruction
---

# Edit-aware RAW Reconstruction
**arXiv**：[2512.05859v1](https://arxiv.org/abs/2512.05859) · [PDF](https://arxiv.org/pdf/2512.05859.pdf)  
**作者**：Abhijith Punnappurath, Luxi Zhao, Ke Zhao, Hue Nguyen, Radek Grzeszczuk, Michael S. Brown  

**一句话要点**：提出编辑感知损失函数以增强RAW重建在多样化渲染和编辑下的鲁棒性

**关键词**：RAW重建, 编辑感知损失, 可微分ISP, 光处理模拟, sRGB重建, 编辑鲁棒性

## 3 点简述
- 核心问题：现有RAW重建方法在多样化渲染风格和编辑操作下性能下降
- 方法要点：集成可微分ISP模拟真实光处理，通过随机采样参数训练编辑感知损失
- 实验或效果：提升sRGB重建质量达1.5-2 dB PSNR，支持针对目标编辑的微调

## 摘要（原文）

> Users frequently edit camera images post-capture to achieve their preferred photofinishing style. While editing in the RAW domain provides greater accuracy and flexibility, most edits are performed on the camera's display-referred output (e.g., 8-bit sRGB JPEG) since RAW images are rarely stored. Existing RAW reconstruction methods can recover RAW data from sRGB images, but these approaches are typically optimized for pixel-wise RAW reconstruction fidelity and tend to degrade under diverse rendering styles and editing operations. We introduce a plug-and-play, edit-aware loss function that can be integrated into any existing RAW reconstruction framework to make the recovered RAWs more robust to different rendering styles and edits. Our loss formulation incorporates a modular, differentiable image signal processor (ISP) that simulates realistic photofinishing pipelines with tunable parameters. During training, parameters for each ISP module are randomly sampled from carefully designed distributions that model practical variations in real camera processing. The loss is then computed in sRGB space between ground-truth and reconstructed RAWs rendered through this differentiable ISP. Incorporating our loss improves sRGB reconstruction quality by up to 1.5-2 dB PSNR across various editing conditions. Moreover, when applied to metadata-assisted RAW reconstruction methods, our approach enables fine-tuning for target edits, yielding further gains. Since photographic editing is the primary motivation for RAW reconstruction in consumer imaging, our simple yet effective loss function provides a general mechanism for enhancing edit fidelity and rendering flexibility across existing methods.

