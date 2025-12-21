---
layout: default
title: StereoPilot: Learning Unified and Efficient Stereo Conversion via Generative Priors
---

# StereoPilot: Learning Unified and Efficient Stereo Conversion via Generative Priors
**arXiv**：[2512.16915v1](https://arxiv.org/abs/2512.16915) · [PDF](https://arxiv.org/pdf/2512.16915.pdf)  
**作者**：Guibao Shen, Yihua Du, Wenhang Ge, Jing He, Chirui Chang, Donghao Zhou, Zhen Yang, Luozhou Wang, Xin Tao, Ying-Cong Chen  

**一句话要点**：提出StereoPilot模型，通过生成先验实现高效统一的单目到立体视频转换。

**关键词**：立体视频转换, 生成先验, 单目到立体, 前馈模型, 数据集构建

## 3 点简述
- 核心问题：传统多阶段深度-扭曲-修复方法存在误差传播、深度模糊和格式不一致问题。
- 方法要点：基于UniStereo数据集，设计前馈模型直接合成目标视图，无需显式深度图或迭代扩散采样。
- 实验或效果：在视觉保真度和计算效率上显著优于现有方法，支持不同立体格式自适应转换。

## 摘要（原文）

> The rapid growth of stereoscopic displays, including VR headsets and 3D cinemas, has led to increasing demand for high-quality stereo video content. However, producing 3D videos remains costly and complex, while automatic Monocular-to-Stereo conversion is hindered by the limitations of the multi-stage ``Depth-Warp-Inpaint'' (DWI) pipeline. This paradigm suffers from error propagation, depth ambiguity, and format inconsistency between parallel and converged stereo configurations. To address these challenges, we introduce UniStereo, the first large-scale unified dataset for stereo video conversion, covering both stereo formats to enable fair benchmarking and robust model training. Building upon this dataset, we propose StereoPilot, an efficient feed-forward model that directly synthesizes the target view without relying on explicit depth maps or iterative diffusion sampling. Equipped with a learnable domain switcher and a cycle consistency loss, StereoPilot adapts seamlessly to different stereo formats and achieves improved consistency. Extensive experiments demonstrate that StereoPilot significantly outperforms state-of-the-art methods in both visual fidelity and computational efficiency. Project page: https://hit-perfect.github.io/StereoPilot/.

