---
layout: default
title: AlphaFace: High Fidelity and Real-time Face Swapper Robust to Facial Pose
---

# AlphaFace: High Fidelity and Real-time Face Swapper Robust to Facial Pose
**arXiv**：[2601.16429v1](https://arxiv.org/abs/2601.16429) · [PDF](https://arxiv.org/pdf/2601.16429.pdf)  
**作者**：Jongmin Yu, Hyeontaek Oh, Zhongtian Sun, Angelica I Aviles-Rivero, Moongu Jeon, Jinhong Yang  

**一句话要点**：提出AlphaFace以解决极端面部姿态下换脸质量下降问题，实现高保真实时换脸。

**关键词**：人脸交换, 姿态鲁棒性, 视觉语言模型, 对比学习, 实时处理

## 3 点简述
- 现有方法在极端面部姿态下换脸质量显著下降，几何特征方法增加计算成本。
- 利用开源视觉语言模型和CLIP嵌入，引入视觉与文本语义对比损失，增强身份表示和属性保留。
- 在FF++、MPIE和LPFF数据集上实验，AlphaFace在姿态挑战案例中超越现有方法，保持实时性能。

## 摘要（原文）

> Existing face-swapping methods often deliver competitive results in constrained settings but exhibit substantial quality degradation when handling extreme facial poses. To improve facial pose robustness, explicit geometric features are applied, but this approach remains problematic since it introduces additional dependencies and increases computational cost. Diffusion-based methods have achieved remarkable results; however, they are impractical for real-time processing. We introduce AlphaFace, which leverages an open-source vision-language model and CLIP image and text embeddings to apply novel visual and textual semantic contrastive losses. AlphaFace enables stronger identity representation and more precise attribute preservation, all while maintaining real-time performance. Comprehensive experiments across FF++, MPIE, and LPFF demonstrate that AlphaFace surpasses state-of-the-art methods in pose-challenging cases. The project is publicly available on `https://github.com/andrewyu90/Alphaface_Official.git'.

