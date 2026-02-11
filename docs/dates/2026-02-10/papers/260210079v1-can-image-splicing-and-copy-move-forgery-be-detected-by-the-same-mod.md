---
layout: default
title: Can Image Splicing and Copy-Move Forgery Be Detected by the Same Model? Forensim: An Attention-Based State-Space Approach
---

# Can Image Splicing and Copy-Move Forgery Be Detected by the Same Model? Forensim: An Attention-Based State-Space Approach
**arXiv**：[2602.10079v1](https://arxiv.org/abs/2602.10079) · [PDF](https://arxiv.org/pdf/2602.10079.pdf)  
**作者**：Soumyaroop Nandi, Prem Natarajan  

**一句话要点**：提出Forensim注意力状态空间框架，以联合定位图像篡改源区和目标区，解决传统方法依赖单一线索的问题。

**关键词**：图像伪造检测, 注意力机制, 状态空间模型, 联合定位, 端到端训练, 数据集构建

## 3 点简述
- 核心问题：传统图像伪造检测仅依赖伪影线索，无法联合定位源区和目标区，易误导解读。
- 方法要点：基于视觉状态空间模型，利用归一化注意力图捕捉内部相似性，结合区域块注意力模块区分篡改区域。
- 实验或效果：在标准基准测试中达到最先进性能，并发布新数据集CMFD-Anything以弥补现有不足。

## 摘要（原文）

> We introduce Forensim, an attention-based state-space framework for image forgery detection that jointly localizes both manipulated (target) and source regions. Unlike traditional approaches that rely solely on artifact cues to detect spliced or forged areas, Forensim is designed to capture duplication patterns crucial for understanding context. In scenarios such as protest imagery, detecting only the forged region, for example a duplicated act of violence inserted into a peaceful crowd, can mislead interpretation, highlighting the need for joint source-target localization. Forensim outputs three-class masks (pristine, source, target) and supports detection of both splicing and copy-move forgeries within a unified architecture. We propose a visual state-space model that leverages normalized attention maps to identify internal similarities, paired with a region-based block attention module to distinguish manipulated regions. This design enables end-to-end training and precise localization. Forensim achieves state-of-the-art performance on standard benchmarks. We also release CMFD-Anything, a new dataset addressing limitations of existing copy-move forgery datasets.

