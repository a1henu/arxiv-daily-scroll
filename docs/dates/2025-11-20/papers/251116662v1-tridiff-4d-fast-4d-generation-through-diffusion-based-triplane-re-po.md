---
layout: default
title: TriDiff-4D: Fast 4D Generation through Diffusion-based Triplane Re-posing
---

# TriDiff-4D: Fast 4D Generation through Diffusion-based Triplane Re-posing
**arXiv**：[2511.16662v1](https://arxiv.org/abs/2511.16662) · [PDF](https://arxiv.org/pdf/2511.16662.pdf)  
**作者**：Eddie Pokming Sheung, Qihao Liu, Wufei Ma, Prakhar Kaushik, Jianwen Xie, Alan Yuille  

**一句话要点**：提出TriDiff-4D，通过扩散基三平面重定位解决4D化身生成中的一致性与效率问题

**关键词**：4D生成, 扩散模型, 三平面表示, 运动控制, 计算效率

## 3 点简述
- 核心问题：现有4D生成方法存在时空不一致、运动不规则和高计算成本等局限
- 方法要点：采用自回归扩散模型，结合3D结构和运动先验，实现骨架驱动的4D生成
- 实验或效果：显著减少生成时间至秒级，提升运动准确性和视觉保真度

## 摘要（原文）

> With the increasing demand for 3D animation, generating high-fidelity, controllable 4D avatars from textual descriptions remains a significant challenge. Despite notable efforts in 4D generative modeling, existing methods exhibit fundamental limitations that impede their broader applicability, including temporal and geometric inconsistencies, perceptual artifacts, motion irregularities, high computational costs, and limited control over dynamics. To address these challenges, we propose TriDiff-4D, a novel 4D generative pipeline that employs diffusion-based triplane re-posing to produce high-quality, temporally coherent 4D avatars. Our model adopts an auto-regressive strategy to generate 4D sequences of arbitrary length, synthesizing each 3D frame with a single diffusion process. By explicitly learning 3D structure and motion priors from large-scale 3D and motion datasets, TriDiff-4D enables skeleton-driven 4D generation that excels in temporal consistency, motion accuracy, computational efficiency, and visual fidelity. Specifically, TriDiff-4D first generates a canonical 3D avatar and a corresponding motion sequence from a text prompt, then uses a second diffusion model to animate the avatar according to the motion sequence, supporting arbitrarily long 4D generation. Experimental results demonstrate that TriDiff-4D significantly outperforms existing methods, reducing generation time from hours to seconds by eliminating the optimization process, while substantially improving the generation of complex motions with high-fidelity appearance and accurate 3D geometry.

