---
layout: default
title: UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models
---

# UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models
**arXiv**：[2602.22960v1](https://arxiv.org/abs/2602.22960) · [PDF](https://arxiv.org/pdf/2602.22960.pdf)  
**作者**：Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang  

**一句话要点**：提出UCM框架，通过时间感知位置编码扭曲机制统一长时记忆与精确相机控制，用于世界模型视频生成。

**关键词**：世界模型, 视频生成, 相机控制, 长时记忆, 位置编码, 扩散Transformer

## 3 点简述
- 核心问题：世界模型在长时内容一致性和用户输入相机控制方面存在困难，现有方法在灵活性和可控性上受限。
- 方法要点：采用时间感知位置编码扭曲机制，结合高效双流扩散Transformer，并利用点云渲染进行数据增强。
- 实验或效果：在真实和合成基准测试中，UCM在长时场景一致性和高保真视频生成的相机可控性上显著优于现有方法。

## 摘要（原文）

> World models based on video generation demonstrate remarkable potential for simulating interactive environments but face persistent difficulties in two key areas: maintaining long-term content consistency when scenes are revisited and enabling precise camera control from user-provided inputs. Existing methods based on explicit 3D reconstruction often compromise flexibility in unbounded scenarios and fine-grained structures. Alternative methods rely directly on previously generated frames without establishing explicit spatial correspondence, thereby constraining controllability and consistency. To address these limitations, we present UCM, a novel framework that unifies long-term memory and precise camera control via a time-aware positional encoding warping mechanism. To reduce computational overhead, we design an efficient dual-stream diffusion transformer for high-fidelity generation. Moreover, we introduce a scalable data curation strategy utilizing point-cloud-based rendering to simulate scene revisiting, facilitating training on over 500K monocular videos. Extensive experiments on real-world and synthetic benchmarks demonstrate that UCM significantly outperforms state-of-the-art methods in long-term scene consistency, while also achieving precise camera controllability in high-fidelity video generation.

