---
layout: default
title: Ovis-Image Technical Report
---

# Ovis-Image Technical Report
**arXiv**：[2511.22982v1](https://arxiv.org/abs/2511.22982) · [PDF](https://arxiv.org/pdf/2511.22982.pdf)  
**作者**：Guo-Hua Wang, Liangfu Cao, Tianyu Cui, Minghao Fu, Xiaohao Chen, Pengxin Zhan, Jianshan Zhao, Lan Li, Bowen Fu, Jiaqi Liu, Qing-Guo Chen  

**一句话要点**：提出Ovis-Image以在有限计算资源下实现高质量文本渲染

**关键词**：文本到图像生成, 文本渲染优化, 多模态骨干网络, 扩散模型, 高效部署

## 3 点简述
- 核心问题：在严格计算约束下实现高质量文本渲染，缩小前沿性能与实用部署的差距。
- 方法要点：基于Ovis-U1框架，集成扩散视觉解码器和Ovis 2.5多模态骨干，采用以文本为中心的训练流程。
- 实验或效果：在文本渲染性能上媲美更大开源模型，接近闭源系统，可在单高端GPU上部署。

## 摘要（原文）

> We introduce $\textbf{Ovis-Image}$, a 7B text-to-image model specifically optimized for high-quality text rendering, designed to operate efficiently under stringent computational constraints. Built upon our previous Ovis-U1 framework, Ovis-Image integrates a diffusion-based visual decoder with the stronger Ovis 2.5 multimodal backbone, leveraging a text-centric training pipeline that combines large-scale pre-training with carefully tailored post-training refinements. Despite its compact architecture, Ovis-Image achieves text rendering performance on par with significantly larger open models such as Qwen-Image and approaches closed-source systems like Seedream and GPT4o. Crucially, the model remains deployable on a single high-end GPU with moderate memory, narrowing the gap between frontier-level text rendering and practical deployment. Our results indicate that combining a strong multimodal backbone with a carefully designed, text-focused training recipe is sufficient to achieve reliable bilingual text rendering without resorting to oversized or proprietary models.

