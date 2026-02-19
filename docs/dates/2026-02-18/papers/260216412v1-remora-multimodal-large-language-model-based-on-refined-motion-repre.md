---
layout: default
title: ReMoRa: Multimodal Large Language Model based on Refined Motion Representation for Long-Video Understanding
---

# ReMoRa: Multimodal Large Language Model based on Refined Motion Representation for Long-Video Understanding
**arXiv**：[2602.16412v1](https://arxiv.org/abs/2602.16412) · [PDF](https://arxiv.org/pdf/2602.16412.pdf)  
**作者**：Daichi Yashima, Shuhei Kurita, Yusuke Oda, Komei Sugiura  

**一句话要点**：提出ReMoRa，基于精炼运动表示的多模态大语言模型，用于长视频理解

**关键词**：长视频理解, 多模态大语言模型, 运动表示, 视频压缩, 自注意力机制, 基准测试

## 3 点简述
- 核心问题：长视频理解中处理RGB帧序列计算成本高且冗余，自注意力机制复杂度为二次方。
- 方法要点：使用压缩表示处理视频，保留稀疏RGB关键帧用于外观，编码运动表示捕获时间动态，无需全帧解码。
- 实验或效果：在LongVideoBench、NExT-QA和MLVU等基准测试中优于基线方法，验证了有效性。

## 摘要（原文）

> While multimodal large language models (MLLMs) have shown remarkable success across a wide range of tasks, long-form video understanding remains a significant challenge. In this study, we focus on video understanding by MLLMs. This task is challenging because processing a full stream of RGB frames is computationally intractable and highly redundant, as self-attention have quadratic complexity with sequence length. In this paper, we propose ReMoRa, a video MLLM that processes videos by operating directly on their compressed representations. A sparse set of RGB keyframes is retained for appearance, while temporal dynamics are encoded as a motion representation, removing the need for sequential RGB frames. These motion representations act as a compact proxy for optical flow, capturing temporal dynamics without full frame decoding. To refine the noise and low fidelity of block-based motions, we introduce a module to denoise and generate a fine-grained motion representation. Furthermore, our model compresses these features in a way that scales linearly with sequence length. We demonstrate the effectiveness of ReMoRa through extensive experiments across a comprehensive suite of long-video understanding benchmarks. ReMoRa outperformed baseline methods on multiple challenging benchmarks, including LongVideoBench, NExT-QA, and MLVU.

