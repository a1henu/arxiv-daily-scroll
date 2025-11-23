---
layout: default
title: FastSurfer-CC: A robust, accurate, and comprehensive framework for corpus callosum morphometry
---

# FastSurfer-CC: A robust, accurate, and comprehensive framework for corpus callosum morphometry
**arXiv**：[2511.16471v1](https://arxiv.org/abs/2511.16471) · [PDF](https://arxiv.org/pdf/2511.16471.pdf)  
**作者**：Clemens Pollak, Kersten Diers, Santiago Estrada, David Kügler, Martin Reuter  

**一句话要点**：提出FastSurfer-CC框架以自动化胼胝体形态测量，用于脑老化和神经疾病研究。

**关键词**：胼胝体分割, 脑形态测量, 自动化框架, 神经影像分析, 亨廷顿病研究

## 3 点简述
- 核心问题：缺乏公开、全面的自动化胼胝体分割与分析工具。
- 方法要点：自动识别中矢状面、分割胼胝体和穹窿，并提取形状指标。
- 实验或效果：在亨廷顿病中检测到现有方法未发现的显著差异。

## 摘要（原文）

> The corpus callosum, the largest commissural structure in the human brain, is a central focus in research on aging and neurological diseases. It is also a critical target for interventions such as deep brain stimulation and serves as an important biomarker in clinical trials, including those investigating remyelination therapies. Despite extensive research on corpus callosum segmentation, few publicly available tools provide a comprehensive and automated analysis pipeline. To address this gap, we present FastSurfer-CC, an efficient and fully automated framework for corpus callosum morphometry. FastSurfer-CC automatically identifies mid-sagittal slices, segments the corpus callosum and fornix, localizes the anterior and posterior commissures to standardize head positioning, generates thickness profiles and subdivisions, and extracts eight shape metrics for statistical analysis. We demonstrate that FastSurfer-CC outperforms existing specialized tools across the individual tasks. Moreover, our method reveals statistically significant differences between Huntington's disease patients and healthy controls that are not detected by the current state-of-the-art.

