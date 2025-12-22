---
layout: default
title: Region-Constraint In-Context Generation for Instructional Video Editing
---

# Region-Constraint In-Context Generation for Instructional Video Editing
**arXiv**：[2512.17650v1](https://arxiv.org/abs/2512.17650) · [PDF](https://arxiv.org/pdf/2512.17650.pdf)  
**作者**：Zhongwei Zhang, Fuchen Long, Wei Li, Zhaofan Qiu, Wu Liu, Ting Yao, Tao Mei  

**一句话要点**：提出ReCo范式以解决指令视频编辑中的区域不准确和干扰问题

**关键词**：指令视频编辑, 上下文生成, 区域约束, 扩散模型, 正则化, 视频数据集

## 3 点简述
- 核心问题：指令视频编辑中未指定编辑区域导致编辑不准确和去噪时编辑与非编辑区域间的令牌干扰
- 方法要点：通过宽度拼接源与目标视频进行联合去噪，并引入潜在和注意力正则化校准扩散学习
- 实验或效果：在四个主要指令视频编辑任务上实验验证了优越性，并构建了大规模高质量数据集ReCo-Data

## 摘要（原文）

> The In-context generation paradigm recently has demonstrated strong power in instructional image editing with both data efficiency and synthesis quality. Nevertheless, shaping such in-context learning for instruction-based video editing is not trivial. Without specifying editing regions, the results can suffer from the problem of inaccurate editing regions and the token interference between editing and non-editing areas during denoising. To address these, we present ReCo, a new instructional video editing paradigm that novelly delves into constraint modeling between editing and non-editing regions during in-context generation. Technically, ReCo width-wise concatenates source and target video for joint denoising. To calibrate video diffusion learning, ReCo capitalizes on two regularization terms, i.e., latent and attention regularization, conducting on one-step backward denoised latents and attention maps, respectively. The former increases the latent discrepancy of the editing region between source and target videos while reducing that of non-editing areas, emphasizing the modification on editing area and alleviating outside unexpected content generation. The latter suppresses the attention of tokens in the editing region to the tokens in counterpart of the source video, thereby mitigating their interference during novel object generation in target video. Furthermore, we propose a large-scale, high-quality video editing dataset, i.e., ReCo-Data, comprising 500K instruction-video pairs to benefit model training. Extensive experiments conducted on four major instruction-based video editing tasks demonstrate the superiority of our proposal.

