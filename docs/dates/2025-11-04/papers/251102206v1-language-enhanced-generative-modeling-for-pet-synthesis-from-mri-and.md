---
layout: default
title: Language-Enhanced Generative Modeling for PET Synthesis from MRI and Blood Biomarkers
---

# Language-Enhanced Generative Modeling for PET Synthesis from MRI and Blood Biomarkers
**arXiv**：[2511.02206v1](https://arxiv.org/abs/2511.02206) · [PDF](https://arxiv.org/pdf/2511.02206.pdf)  
**作者**：Zhengjie Zhang, Xiaoxie Mao, Qihao Guo, Shaoting Zhang, Qi Huang, Mu Zhou, Fang Xie, Mianxin Liu  

**一句话要点**：提出语言增强生成模型，从MRI和血液生物标志物合成PET图像以改进阿尔茨海默病诊断

**关键词**：PET图像合成, 多模态融合, 阿尔茨海默病诊断, 语言增强生成模型, 血液生物标志物

## 3 点简述
- 核心问题：阿尔茨海默病诊断依赖高成本PET，需从MRI和血液生物标志物预测PET空间模式
- 方法要点：开发语言增强生成模型，融合大语言模型和多模态信息合成PET图像
- 实验或效果：合成PET图像质量高，诊断准确率达0.80，AUC优于基线模型

## 摘要（原文）

> Background: Alzheimer's disease (AD) diagnosis heavily relies on amyloid-beta
> positron emission tomography (Abeta-PET), which is limited by high cost and
> limited accessibility. This study explores whether Abeta-PET spatial patterns
> can be predicted from blood-based biomarkers (BBMs) and MRI scans. Methods: We
> collected Abeta-PET images, T1-weighted MRI scans, and BBMs from 566
> participants. A language-enhanced generative model, driven by a large language
> model (LLM) and multimodal information fusion, was developed to synthesize PET
> images. Synthesized images were evaluated for image quality, diagnostic
> consistency, and clinical applicability within a fully automated diagnostic
> pipeline. Findings: The synthetic PET images closely resemble real PET scans in
> both structural details (SSIM = 0.920 +/- 0.003) and regional patterns
> (Pearson's r = 0.955 +/- 0.007). Diagnostic outcomes using synthetic PET show
> high agreement with real PET-based diagnoses (accuracy = 0.80). Using synthetic
> PET, we developed a fully automatic AD diagnostic pipeline integrating PET
> synthesis and classification. The synthetic PET-based model (AUC = 0.78)
> outperforms T1-based (AUC = 0.68) and BBM-based (AUC = 0.73) models, while
> combining synthetic PET and BBMs further improved performance (AUC = 0.79).
> Ablation analysis supports the advantages of LLM integration and prompt
> engineering. Interpretation: Our language-enhanced generative model synthesizes
> realistic PET images, enhancing the utility of MRI and BBMs for Abeta spatial
> pattern assessment and improving the diagnostic workflow for Alzheimer's
> disease.

