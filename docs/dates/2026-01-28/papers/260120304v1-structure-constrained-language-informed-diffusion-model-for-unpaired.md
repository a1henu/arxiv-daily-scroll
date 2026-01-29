---
layout: default
title: Structure-constrained Language-informed Diffusion Model for Unpaired Low-dose Computed Tomography Angiography Reconstruction
---

# Structure-constrained Language-informed Diffusion Model for Unpaired Low-dose Computed Tomography Angiography Reconstruction
**arXiv**：[2601.20304v1](https://arxiv.org/abs/2601.20304) · [PDF](https://arxiv.org/pdf/2601.20304.pdf)  
**作者**：Genyuan Zhang, Zihao Wang, Zhifan Gao, Lei Xu, Zhen Zhou, Haijun Yu, Jianjia Zhang, Xiujian Liu, Weiwei Zhang, Shaoyu Wang, Huazhu Fu, Fenglin Liu, Weiwen Wu  

**一句话要点**：提出结构约束语言引导扩散模型以解决非配对低剂量CT血管造影重建问题

**关键词**：低剂量CT血管造影, 非配对图像增强, 扩散模型, 结构约束, 语义监督, 医学图像生成

## 3 点简述
- 核心问题：非配对低剂量CT图像难以实现准确增强，因模型识别特定结构能力有限
- 方法要点：结合结构先验信息与空间智能语义监督，确保增强过程的结构一致性和准确性
- 实验或效果：通过视觉比较和定量指标验证，在低剂量对比剂CT血管造影重建中表现有效

## 摘要（原文）

> The application of iodinated contrast media (ICM) improves the sensitivity and specificity of computed tomography (CT) for a wide range of clinical indications. However, overdose of ICM can cause problems such as kidney damage and life-threatening allergic reactions. Deep learning methods can generate CT images of normal-dose ICM from low-dose ICM, reducing the required dose while maintaining diagnostic power. However, existing methods are difficult to realize accurate enhancement with incompletely paired images, mainly because of the limited ability of the model to recognize specific structures. To overcome this limitation, we propose a Structure-constrained Language-informed Diffusion Model (SLDM), a unified medical generation model that integrates structural synergy and spatial intelligence. First, the structural prior information of the image is effectively extracted to constrain the model inference process, thus ensuring structural consistency in the enhancement process. Subsequently, semantic supervision strategy with spatial intelligence is introduced, which integrates the functions of visual perception and spatial reasoning, thus prompting the model to achieve accurate enhancement. Finally, the subtraction angiography enhancement module is applied, which serves to improve the contrast of the ICM agent region to suitable interval for observation. Qualitative analysis of visual comparison and quantitative results of several metrics demonstrate the effectiveness of our method in angiographic reconstruction for low-dose contrast medium CT angiography.

