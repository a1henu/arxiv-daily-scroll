---
layout: default
title: HaineiFRDM: Explore Diffusion to Restore Defects in Fast-Movement Films
---

# HaineiFRDM: Explore Diffusion to Restore Defects in Fast-Movement Films
**arXiv**：[2512.24946v1](https://arxiv.org/abs/2512.24946) · [PDF](https://arxiv.org/pdf/2512.24946.pdf)  
**作者**：Rongji Xun, Junjie Yuan, Zhongjie Wang  

**一句话要点**：提出HaineiFRDM扩散模型框架，以修复快速运动影片中的缺陷

**关键词**：影片修复, 扩散模型, 高分辨率处理, 分块训练, 纹理一致性, 数据集构建

## 3 点简述
- 开源方法因低质量合成数据和噪声光流训练，修复性能有限，且未探索高分辨率影片。
- 采用分块训练测试策略，结合全局提示和帧融合模块，并引入全局-局部频率模块以保持纹理一致性。
- 构建包含真实退化影片和合成数据的修复数据集，实验显示模型在缺陷修复能力上优于现有开源方法。

## 摘要（原文）

> Existing open-source film restoration methods show limited performance compared to commercial methods due to training with low-quality synthetic data and employing noisy optical flows. In addition, high-resolution films have not been explored by the open-source methods.We propose HaineiFRDM(Film Restoration Diffusion Model), a film restoration framework, to explore diffusion model's powerful content-understanding ability to help human expert better restore indistinguishable film defects.Specifically, we employ a patch-wise training and testing strategy to make restoring high-resolution films on one 24GB-VRAMR GPU possible and design a position-aware Global Prompt and Frame Fusion Modules.Also, we introduce a global-local frequency module to reconstruct consistent textures among different patches. Besides, we firstly restore a low-resolution result and use it as global residual to mitigate blocky artifacts caused by patching process.Furthermore, we construct a film restoration dataset that contains restored real-degraded films and realistic synthetic data.Comprehensive experimental results conclusively demonstrate the superiority of our model in defect restoration ability over existing open-source methods. Code and the dataset will be released.

