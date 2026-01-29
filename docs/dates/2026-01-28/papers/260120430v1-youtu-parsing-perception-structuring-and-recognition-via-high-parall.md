---
layout: default
title: Youtu-Parsing: Perception, Structuring and Recognition via High-Parallelism Decoding
---

# Youtu-Parsing: Perception, Structuring and Recognition via High-Parallelism Decoding
**arXiv**：[2601.20430v1](https://arxiv.org/abs/2601.20430) · [PDF](https://arxiv.org/pdf/2601.20430.pdf)  
**作者**：Kun Yin, Yunfei Wu, Bing Liu, Zhongpeng Cai, Xiaotian Li, Huang Chen, Xin Li, Haoyu Cao, Yinsong Liu, Deqiang Jiang, Xing Sun, Yunsheng Wu, Qianyu Li, Antai Guo, Yanzhen Liao, Yanqiu Qu, Haodong Lin, Chengxu He, Shuangyin Liu  

**一句话要点**：提出Youtu-Parsing模型，通过高并行解码策略实现高效文档解析，适用于大规模文档智能应用。

**关键词**：文档解析, 高并行解码, 视觉Transformer, 语言模型, 表格识别, 多语言文本处理

## 3 点简述
- 核心问题：文档解析需高效提取多种元素，传统自回归解码速度慢，影响大规模应用。
- 方法要点：采用动态分辨率视觉编码器提取共享特征，结合提示引导语言模型，引入令牌并行和查询并行解码策略加速推理。
- 实验或效果：在OmniDocBench和olmOCR-bench基准上达到SOTA性能，解码速度提升5-11倍，保持输出质量。

## 摘要（原文）

> This paper presents Youtu-Parsing, an efficient and versatile document parsing model designed for high-performance content extraction. The architecture employs a native Vision Transformer (ViT) featuring a dynamic-resolution visual encoder to extract shared document features, coupled with a prompt-guided Youtu-LLM-2B language model for layout analysis and region-prompted decoding. Leveraging this decoupled and feature-reusable framework, we introduce a high-parallelism decoding strategy comprising two core components: token parallelism and query parallelism. The token parallelism strategy concurrently generates up to 64 candidate tokens per inference step, which are subsequently validated through a verification mechanism. This approach yields a 5--11x speedup over traditional autoregressive decoding and is particularly well-suited for highly structured scenarios, such as table recognition. To further exploit the advantages of region-prompted decoding, the query parallelism strategy enables simultaneous content prediction for multiple bounding boxes (up to five), providing an additional 2x acceleration while maintaining output quality equivalent to standard decoding. Youtu-Parsing encompasses a diverse range of document elements, including text, formulas, tables, charts, seals, and hierarchical structures. Furthermore, the model exhibits strong robustness when handling rare characters, multilingual text, and handwritten content. Extensive evaluations demonstrate that Youtu-Parsing achieves state-of-the-art (SOTA) performance on both the OmniDocBench and olmOCR-bench benchmarks. Overall, Youtu-Parsing demonstrates significant experimental value and practical utility for large-scale document intelligence applications.

