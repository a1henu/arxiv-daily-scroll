---
layout: default
title: Text-guided Controllable Diffusion for Realistic Camouflage Images Generation
---

# Text-guided Controllable Diffusion for Realistic Camouflage Images Generation
**arXiv**：[2511.20218v1](https://arxiv.org/abs/2511.20218) · [PDF](https://arxiv.org/pdf/2511.20218.pdf)  
**作者**：Yuhang Qian, Haiyan Chen, Wentong Li, Ningzhong Liu, Jie Qin  

**一句话要点**：提出可控文本引导扩散方法以生成逼真伪装图像

**关键词**：伪装图像生成, 文本引导扩散, 视觉语言模型, 频率特征交互, 可控生成

## 3 点简述
- 现有方法忽视伪装对象与背景的逻辑关系，导致结果不自然
- 利用视觉语言模型标注数据集，微调扩散模型并加入控制器和频率模块
- 实验显示文本提示语义对齐，能生成逼真且有效的伪装图像

## 摘要（原文）

> Camouflage Images Generation (CIG) is an emerging research area that focuses on synthesizing images in which objects are harmoniously blended and exhibit high visual consistency with their surroundings. Existing methods perform CIG by either fusing objects into specific backgrounds or outpainting the surroundings via foreground object-guided diffusion. However, they often fail to obtain natural results because they overlook the logical relationship between camouflaged objects and background environments. To address this issue, we propose CT-CIG, a Controllable Text-guided Camouflage Images Generation method that produces realistic and logically plausible camouflage images. Leveraging Large Visual Language Models (VLM), we design a Camouflage-Revealing Dialogue Mechanism (CRDM) to annotate existing camouflage datasets with high-quality text prompts. Subsequently, the constructed image-prompt pairs are utilized to finetune Stable Diffusion, incorporating a lightweight controller to guide the location and shape of camouflaged objects for enhanced camouflage scene fitness. Moreover, we design a Frequency Interaction Refinement Module (FIRM) to capture high-frequency texture features, facilitating the learning of complex camouflage patterns. Extensive experiments, including CLIPScore evaluation and camouflage effectiveness assessment, demonstrate the semantic alignment of our generated text prompts and CT-CIG's ability to produce photorealistic camouflage images.

