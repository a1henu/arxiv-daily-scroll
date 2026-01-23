---
layout: default
title: PMPBench: A Paired Multi-Modal Pan-Cancer Benchmark for Medical Image Synthesis
---

# PMPBench: A Paired Multi-Modal Pan-Cancer Benchmark for Medical Image Synthesis
**arXiv**：[2601.15884v1](https://arxiv.org/abs/2601.15884) · [PDF](https://arxiv.org/pdf/2601.15884.pdf)  
**作者**：Yifan Chen, Fei Yin, Hao Chen, Jia Wu, Chao Li  

**一句话要点**：提出首个公开、全配对、多器官医学影像数据集与基准以解决对比剂合成中的数据限制问题。

**关键词**：医学影像合成, 对比剂增强, 多模态数据集, 图像翻译基准, 肿瘤成像

## 3 点简述
- 核心问题：现有医学影像合成数据集局限于脑部、配对不完整或缺乏标注，阻碍AI在肿瘤诊断中的应用。
- 方法要点：构建包含11个器官的MR和CT全配对数据集，支持1对1、N对1和N对N图像翻译任务。
- 实验或效果：基于数据集建立基准，评估代表性图像翻译方法，促进安全有效的对比剂合成研究。

## 摘要（原文）

> Contrast medium plays a pivotal role in radiological imaging, as it amplifies lesion conspicuity and improves detection for the diagnosis of tumor-related diseases. However, depending on the patient's health condition or the medical resources available, the use of contrast medium is not always feasible. Recent work has explored AI-based image translation to synthesize contrast-enhanced images directly from non-contrast scans, aims to reduce side effects and streamlines clinical workflows. Progress in this direction has been constrained by data limitations: (1) existing public datasets focus almost exclusively on brain-related paired MR modalities; (2) other collections include partially paired data but suffer from missing modalities/timestamps and imperfect spatial alignment; (3) explicit labeling of CT vs. CTC or DCE phases is often absent; (4) substantial resources remain private. To bridge this gap, we introduce the first public, fully paired, pan-cancer medical imaging dataset spanning 11 human organs. The MR data include complete dynamic contrast-enhanced (DCE) sequences covering all three phases (DCE1-DCE3), while the CT data provide paired non-contrast and contrast-enhanced acquisitions (CTC). The dataset is curated for anatomical correspondence, enabling rigorous evaluation of 1-to-1, N-to-1, and N-to-N translation settings (e.g., predicting DCE phases from non-contrast inputs). Built upon this resource, we establish a comprehensive benchmark. We report results from representative baselines of contemporary image-to-image translation. We release the dataset and benchmark to catalyze research on safe, effective contrast synthesis, with direct relevance to multi-organ oncology imaging workflows. Our code and dataset are publicly available at https://github.com/YifanChen02/PMPBench.

