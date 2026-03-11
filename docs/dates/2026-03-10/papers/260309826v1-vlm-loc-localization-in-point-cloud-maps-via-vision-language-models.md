---
layout: default
title: VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models
---

# VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models
**arXiv**：[2603.09826v1](https://arxiv.org/abs/2603.09826) · [PDF](https://arxiv.org/pdf/2603.09826.pdf)  
**作者**：Shuhao Kang, Youqi Liao, Peijie Wang, Wenlong Liao, Qilin Zhang, Benjamin Busam, Xieyuanli Chen, Yun Liu  

**一句话要点**：提出VLM-Loc框架，利用视觉语言模型的空间推理能力解决文本到点云定位问题。

**关键词**：文本到点云定位, 视觉语言模型, 空间推理, 场景图, 鸟瞰图, 跨模态表示

## 3 点简述
- 核心问题：现有文本到点云定位方法缺乏有效空间推理，在复杂环境中精度受限。
- 方法要点：将点云转换为鸟瞰图和场景图，结合部分节点分配机制实现跨模态表示与可解释空间推理。
- 实验或效果：在CityLoc基准测试中，VLM-Loc相比先进方法展现出更高的准确性和鲁棒性。

## 摘要（原文）

> Text-to-point-cloud (T2P) localization aims to infer precise spatial positions within 3D point cloud maps from natural language descriptions, reflecting how humans perceive and communicate spatial layouts through language. However, existing methods largely rely on shallow text-point cloud correspondence without effective spatial reasoning, limiting their accuracy in complex environments. To address this limitation, we propose VLM-Loc, a framework that leverages the spatial reasoning capability of large vision-language models (VLMs) for T2P localization. Specifically, we transform point clouds into bird's-eye-view (BEV) images and scene graphs that jointly encode geometric and semantic context, providing structured inputs for the VLM to learn cross-modal representations bridging linguistic and spatial semantics. On top of these representations, we introduce a partial node assignment mechanism that explicitly associates textual cues with scene graph nodes, enabling interpretable spatial reasoning for accurate localization. To facilitate systematic evaluation across diverse scenes, we present CityLoc, a benchmark built from multi-source point clouds for fine-grained T2P localization. Experiments on CityLoc demonstrate VLM-Loc achieves superior accuracy and robustness compared to state-of-the-art methods. Our code, model, and dataset are available at \href{https://github.com/MCG-NKU/nku-3d-vision}{repository}.

