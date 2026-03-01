---
layout: default
title: DrivePTS: A Progressive Learning Framework with Textual and Structural Enhancement for Driving Scene Generation
---

# DrivePTS: A Progressive Learning Framework with Textual and Structural Enhancement for Driving Scene Generation
**arXiv**：[2602.22549v1](https://arxiv.org/abs/2602.22549) · [PDF](https://arxiv.org/pdf/2602.22549.pdf)  
**作者**：Zhechao Wang, Yiming Zeng, Lufan Ma, Zeqing Fu, Chen Bai, Ziyao Lin, Cheng Lu  

**一句话要点**：提出DrivePTS框架，通过渐进学习、文本增强和结构损失提升驾驶场景生成的质量与可控性。

**关键词**：驾驶场景生成, 扩散模型, 渐进学习, 文本增强, 结构损失, 数据增强

## 3 点简述
- 核心问题：现有方法因几何条件间隐式依赖导致生成失败，且语义和结构细节不足，影响背景建模和前景清晰度。
- 方法要点：采用渐进学习策略减少条件依赖，利用视觉语言模型生成多视图文本指导，引入频率引导结构损失增强高频细节。
- 实验或效果：实验显示DrivePTS在生成保真度和可控性上达到先进水平，能生成罕见场景，展现强泛化能力。

## 摘要（原文）

> Synthesis of diverse driving scenes serves as a crucial data augmentation technique for validating the robustness and generalizability of autonomous driving systems. Current methods aggregate high-definition (HD) maps and 3D bounding boxes as geometric conditions in diffusion models for conditional scene generation. However, implicit inter-condition dependency causes generation failures when control conditions change independently. Additionally, these methods suffer from insufficient details in both semantic and structural aspects. Specifically, brief and view-invariant captions restrict semantic contexts, resulting in weak background modeling. Meanwhile, the standard denoising loss with uniform spatial weighting neglects foreground structural details, causing visual distortions and blurriness. To address these challenges, we propose DrivePTS, which incorporates three key innovations. Firstly, our framework adopts a progressive learning strategy to mitigate inter-dependency between geometric conditions, reinforced by an explicit mutual information constraint. Secondly, a Vision-Language Model is utilized to generate multi-view hierarchical descriptions across six semantic aspects, providing fine-grained textual guidance. Thirdly, a frequency-guided structure loss is introduced to strengthen the model's sensitivity to high-frequency elements, improving foreground structural fidelity. Extensive experiments demonstrate that our DrivePTS achieves state-of-the-art fidelity and controllability in generating diverse driving scenes. Notably, DrivePTS successfully generates rare scenes where prior methods fail, highlighting its strong generalization ability.

