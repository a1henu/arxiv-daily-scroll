---
layout: default
title: Enhancing Infrared Vision: Progressive Prompt Fusion Network and Benchmark
---

# Enhancing Infrared Vision: Progressive Prompt Fusion Network and Benchmark
**arXiv**：[2510.09343v1](https://arxiv.org/abs/2510.09343) · [PDF](https://arxiv.org/pdf/2510.09343.pdf)  
**作者**：Jinyuan Liu, Zihang Chen, Zhu Liu, Zhiying Jiang, Long Ma, Xin Fan, Risheng Liu  

**一句话要点**：提出渐进提示融合网络以解决热红外图像耦合退化增强问题

**关键词**：热红外图像增强, 渐进提示融合网络, 耦合退化处理, 选择性渐进训练, 红外基准数据集

## 3 点简述
- 核心问题：现有方法难以处理热红外图像中的耦合退化，如噪声、对比度和模糊
- 方法要点：基于热成像过程建立提示对，通过渐进融合调制特征，自适应处理单或多退化
- 实验或效果：在复杂退化场景中性能提升8.76%，并引入高质量多场景红外基准数据集

## 摘要（原文）

> We engage in the relatively underexplored task named thermal infrared image
> enhancement. Existing infrared image enhancement methods primarily focus on
> tackling individual degradations, such as noise, contrast, and blurring, making
> it difficult to handle coupled degradations. Meanwhile, all-in-one enhancement
> methods, commonly applied to RGB sensors, often demonstrate limited
> effectiveness due to the significant differences in imaging models. In sight of
> this, we first revisit the imaging mechanism and introduce a Progressive Prompt
> Fusion Network (PPFN). Specifically, the PPFN initially establishes prompt
> pairs based on the thermal imaging process. For each type of degradation, we
> fuse the corresponding prompt pairs to modulate the model's features, providing
> adaptive guidance that enables the model to better address specific
> degradations under single or multiple conditions. In addition, a Selective
> Progressive Training (SPT) mechanism is introduced to gradually refine the
> model's handling of composite cases to align the enhancement process, which not
> only allows the model to remove camera noise and retain key structural details,
> but also enhancing the overall contrast of the thermal image. Furthermore, we
> introduce the most high-quality, multi-scenarios infrared benchmark covering a
> wide range of scenarios. Extensive experiments substantiate that our approach
> not only delivers promising visual results under specific degradation but also
> significantly improves performance on complex degradation scenes, achieving a
> notable 8.76\% improvement. Code is available at
> https://github.com/Zihang-Chen/HM-TIR.

